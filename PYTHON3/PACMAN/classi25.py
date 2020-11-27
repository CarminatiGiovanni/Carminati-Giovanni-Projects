import time

class Ghost():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = "down"
        self.cursed = False
        self.status = "pending" # o "pending" o "working"
        self.velox = 3
        self.oldxy = tuple()
        self.bivio = False 
        self.t = time.time()
        self.timeforfreedom = 0
        self.out = False
        
    
    def way(self,map):
        direzioni = list()
        if self.status != "pending":
            if self.direction == "up" or self.direction=="down":
                    #controlli destra e sinistra
                    if map[self.y//16][self.x//16+1] == -2 or map[self.y//16][self.x//16+1] == 2 or map[self.y//16][self.x//16+1] == 3:
                        self.bivio = True
                        direzioni.append("right")
                    if map[self.y//16][self.x//16-1] == -2 or map[self.y//16][self.x//16-1] == 2 or map[self.y//16][self.x//16-1] == 3:
                        self.bivio = True
                        direzioni.append("left")
                    #controlli sopra sotto no self.bivio
                    if map[self.y//16+1][self.x//16] == -2 or map[self.y//16+1][self.x//16] == 2 or map[self.y//16+1][self.x//16] == 3:
                        direzioni.append("down")
                    if map[self.y//16-1][self.x//16] == -2 or map[self.y//16-1][self.x//16] == 2 or map[self.y//16-1][self.x//16] == 3:
                        direzioni.append("up")
                    
            if self.direction == "left" or self.direction=="right": 
                #controlli sopra sotto 
                if map[self.y//16+1][self.x//16] == -2 or map[self.y//16+1][self.x//16] == 2 or map[self.y//16+1][self.x//16] == 3:
                    self.bivio = True
                    direzioni.append("down")
                if map[self.y//16-1][self.x//16] == -2 or map[self.y//16-1][self.x//16] == 2 or map[self.y//16-1][self.x//16] == 3:
                    self.bivio = True
                    direzioni.append("up")
                #controlli destra e sinistra no bivio
                if map[self.y//16][self.x//16+1] == -2 or map[self.y//16][self.x//16+1] == 2 or map[self.y//16][self.x//16+1] == 3:
                    direzioni.append("right")
                if map[self.y//16][self.x//16-1] == -2 or map[self.y//16][self.x//16-1] == 2 or map[self.y//16][self.x//16-1] == 3:
                    direzioni.append("left")
        return direzioni

    def flee(self,direzioni,map,px,py):
        changed=False
        if self.bivio:
            if py >= self.y//16 and px>self.x//16:
                if self.direction == "up" or self.direction == "down":
                    if "left" in direzioni:
                        self.direction = "left"
                        changed = True
                    elif "up" in direzioni:
                        self.direction = "up"
                        changed = True
                elif self.direction == "left" or self.direction == "right":
                    if "up" in direzioni:
                        self.direction = "up"
                        changed = True
                    elif "left" in direzioni:
                        self.direction = "left"
                        changed = True
                if not(changed):
                    self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
            
            if py < self.y//16 and px >= self.x//16:
                if self.direction == "up" or self.direction == "down":
                    if "left" in direzioni:
                        self.direction = "left"
                        changed = True
                    elif "down" in direzioni:
                        self.direction = "down"
                        changed = True
                elif self.direction == "left" or self.direction == "right":
                    if "down" in direzioni:
                        self.direction = "down"
                        changed = True
                    elif "left" in direzioni:
                        self.direction = "left"
                        changed = True
                if not(changed):
                    self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                    
            if py > self.y//16 and px <= self.x//16:
                if self.direction == "up" or self.direction == "down":
                    if "right" in direzioni:
                        self.direction = "right"
                        changed = True
                    elif "up" in direzioni:
                        self.direction = "up"
                        changed = True
                elif self.direction == "left" or self.direction == "right":
                    if "up" in direzioni:
                        self.direction = "up"
                        changed = True
                    elif "right" in direzioni:
                        self.direction = "right"
                        changed = True
                if not(changed):
                    self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
            
            if py <= self.y//16 and px < self.x//16:
                if self.direction == "up" or self.direction == "down":
                    if "right" in direzioni:
                        self.direction = "right"
                        changed = True
                    elif "down" in direzioni:
                        self.direction = "down"
                        changed = True
                elif self.direction == "left" or self.direction == "right":
                    if "down" in direzioni:
                        self.direction = "down"
                        changed = True
                    elif "right" in direzioni:
                        self.direction = "right"
                        changed = True
                if not(changed):
                    self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
        
    def collision(self,px,py):
        if (((py+32)-self.y>4 and (py+32)-self.y<28 and self.x == px) or ((self.y+32)-py>4 and (self.y+32)-py<28 and self.x == px) or (px+32-self.x>4 and px+32-self.x<28 and self.y == py) or (self.x+32-px>4 and self.x+32-px<28 and self.y == py)):       
            return True
        return False

    def setstatus(self):
        if self.x <= 17*16 and self.x >= 12*16 and self.y >= 14*16 and self.y <= 18*16:
            self.status = "pending"
            self.direction = "up"
        else:
            self.status = "working"
            
    def moveghost(self):
        if self.status != "pending":
            if self.x//16 == 0 and self.y//16 == 15:
                self.direction = "right"
            if self.x//16 == 28 and self.y//16 == 15:
                self.direction = "left"   
                
            if self.direction == "left":
                self.x -= self.velox
            elif self.direction == "right":
                self.x += self.velox
            elif self.direction == "down":
                self.y += self.velox
            elif self.direction == "up":
                self.y -= self.velox       
            
            if (self.direction=="left" or self.direction=="right"):
                self.y=(self.y//16)*16 ##corregge la posizione y

            if self.direction=="up" or self.direction=="down":
                self.x=(self.x//16)*16   
        
        #print(f"x = {self.x} y = {self.y}")
                  
class Pizza():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.life = 3
        self.direction = "right"   

class Blinky(Ghost):
    
    def __init__(self,x,y):
        super().__init__(x,y)
        self.not_up_right = True
        self.timeforfreedom = 1
    
    def nextmove(self,px,py,map):
        if self.not_up_right:   #quando nato si sposta in alto a destra
            px = 26
            py = 1
            if self.x//16 == px and self.y//16 == py:
                self.not_up_right = False 
                
        if self.oldxy!=(self.x//16,self.y//16):
            self.bivio = False
            changed = False
            direzioni = super().way(map) #memorizzo le direzioni possibili
            #print(direzioni)
            
            if self.status != "pending":
                if not(self.cursed):
                    if self.status != "pending":
                        if self.bivio:
                            if py >= self.y//16 and px>self.x//16:
                                if self.direction == "up" or self.direction == "down":
                                    if "right" in direzioni:
                                        self.direction = "right"
                                        changed = True
                                    elif "down" in direzioni:
                                        self.direction = "down"
                                        changed = True
                                elif self.direction == "left" or self.direction == "right":
                                    if "down" in direzioni:
                                        self.direction = "down"
                                        changed = True
                                    elif "right" in direzioni:
                                        self.direction = "right"
                                        changed = True
                                if not(changed):
                                    self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                            
                            if py < self.y//16 and px >= self.x//16:
                                if self.direction == "up" or self.direction == "down":
                                    if "right" in direzioni:
                                        self.direction = "right"
                                        changed = True
                                    elif "up" in direzioni:
                                        self.direction = "up"
                                        changed = True
                                elif self.direction == "left" or self.direction == "right":
                                    if "up" in direzioni:
                                        self.direction = "up"
                                        changed = True
                                    elif "right" in direzioni:
                                        self.direction = "right"
                                        changed = True
                                if not(changed):
                                    self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                                    
                            if py > self.y//16 and px <= self.x//16:
                                if self.direction == "up" or self.direction == "down":
                                    if "left" in direzioni:
                                        self.direction = "left"
                                        changed = True
                                    elif "down" in direzioni:
                                        self.direction = "down"
                                        changed = True
                                elif self.direction == "left" or self.direction == "right":
                                    if "down" in direzioni:
                                        self.direction = "down"
                                        changed = True
                                    elif "left" in direzioni:
                                        self.direction = "left"
                                        changed = True
                                if not(changed):
                                    self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                            
                            if py <= self.y//16 and px < self.x//16:
                                if self.direction == "up" or self.direction == "down":
                                    if "left" in direzioni:
                                        self.direction = "left"
                                        changed = True
                                    elif "up" in direzioni:
                                        self.direction = "up"
                                        changed = True
                                elif self.direction == "left" or self.direction == "right":
                                    if "up" in direzioni:
                                        self.direction = "up"
                                        changed = True
                                    elif "left" in direzioni:
                                        self.direction = "left"
                                        changed = True
                                if not(changed):
                                    self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                    
                    elif self.status == "pending":
                        super().pending()
                        
                else:
                    super().flee(direzioni,map,px,py)
            #elif self.status == "pending":
            #    self.y += self.velox
        self.oldxy = (self.x//16,self.y//16)             
        super().moveghost()
        
class Inky(Ghost):

    def __init__(self,x,y):
        super().__init__(x,y)
        self.timeforfreedom = 4

    def nextmove(self,px,py,map,pd,bs):
        if bs == "pending":   #quando nato si sposta in alto a destra
            px = 4
            py = 32
                
        if self.oldxy!=(self.x//16,self.y//16):
            self.bivio = False
            changed = False
            direzioni = super().way(map) #memorizzo le direzioni possibili
            
            if self.status != "pending":
                if not(self.cursed):
                    if abs(px - self.x)>4 and abs(py - self.y)>4:   #se non sei nel raggio di 4 punta 2 celle davanti a te
                        if pd == "up":
                            py-=2
                        elif pd == "down":
                            py+=2
                        elif pd == "left":
                            px-=2
                        elif pd == "right":
                            px+=2
                    
                    if self.bivio:
                        if py > self.y//16 and px >= self.x//16:
                            if self.direction == "up" or self.direction == "down":
                                if "right" in direzioni:
                                    self.direction = "right"
                                    changed = True
                                elif "down" in direzioni:
                                    self.direction = "down"
                                    changed = True
                            elif self.direction == "left" or self.direction == "right":
                                if "down" in direzioni:
                                    self.direction = "down"
                                    changed = True
                                elif "right" in direzioni:
                                    self.direction = "right"
                                    changed = True
                            if not(changed):
                                self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                        
                        if py <= self.y//16 and px > self.x//16:
                            if self.direction == "up" or self.direction == "down":
                                if "right" in direzioni:
                                    self.direction = "right"
                                    changed = True
                                elif "up" in direzioni:
                                    self.direction = "up"
                                    changed = True
                            elif self.direction == "left" or self.direction == "right":
                                if "up" in direzioni:
                                    self.direction = "up"
                                    changed = True
                                elif "right" in direzioni:
                                    self.direction = "right"
                                    changed = True
                            if not(changed):
                                self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                                
                        if py >= self.y//16 and px < self.x//16:
                            if self.direction == "up" or self.direction == "down":
                                if "left" in direzioni:
                                    self.direction = "left"
                                    changed = True
                                elif "down" in direzioni:
                                    self.direction = "down"
                                    changed = True
                            elif self.direction == "left" or self.direction == "right":
                                if "down" in direzioni:
                                    self.direction = "down"
                                    changed = True
                                elif "left" in direzioni:
                                    self.direction = "left"
                                    changed = True
                            if not(changed):
                                self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                        
                        if py < self.y//16 and px <= self.x//16:
                            if self.direction == "up" or self.direction == "down":
                                if "left" in direzioni:
                                    self.direction = "left"
                                    changed = True
                                elif "up" in direzioni:
                                    self.direction = "up"
                                    changed = True
                            elif self.direction == "left" or self.direction == "right":
                                if "up" in direzioni:
                                    self.direction = "up"
                                    changed = True
                                elif "left" in direzioni:
                                    self.direction = "left"
                                    changed = True
                            if not(changed):
                                self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato 
                else:
                    super().flee(direzioni,map,px,py)

            #elif self.status == "pending":
            #    self.y += self.velox
            
                    
        self.oldxy = (self.x//16,self.y//16)             
        super().moveghost()

class Sue(Ghost):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.timeforfreedom = 8
    
    def nextmove(self,px,py,map,pd):
                
        if self.oldxy!=(self.x//16,self.y//16):
            self.bivio = False
            changed = False
            direzioni = super().way(map) #memorizzo le direzioni possibili
    
            if self.status != "pending":
                if not(self.cursed):
                    if pd == "up":
                        py-=12
                    elif pd == "down":
                        py+=12
                    elif pd == "left":
                        px-=12
                    elif pd == "right":
                        px+=12
                        
                    
                    if py >= self.y//16 and px > self.x//16:
                        if self.direction == "up" or self.direction == "down":
                            if "right" in direzioni:
                                self.direction = "right"
                                changed = True
                            elif "down" in direzioni:
                                self.direction = "down"
                                changed = True
                        elif self.direction == "left" or self.direction == "right":
                            if "down" in direzioni:
                                self.direction = "down"
                                changed = True
                            elif "right" in direzioni:
                                self.direction = "right"
                                changed = True
                        if not(changed):
                            self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                    
                    if py < self.y//16 and px >= self.x//16:
                        if self.direction == "up" or self.direction == "down":
                            if "right" in direzioni:
                                self.direction = "right"
                                changed = True
                            elif "up" in direzioni:
                                self.direction = "up"
                                changed = True
                        elif self.direction == "left" or self.direction == "right":
                            if "up" in direzioni:
                                self.direction = "up"
                                changed = True
                            elif "right" in direzioni:
                                self.direction = "right"
                                changed = True
                        if not(changed):
                            self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                            
                    if py > self.y//16 and px <= self.x//16:
                        if self.direction == "up" or self.direction == "down":
                            if "left" in direzioni:
                                self.direction = "left"
                                changed = True
                            elif "down" in direzioni:
                                self.direction = "down"
                                changed = True
                        elif self.direction == "left" or self.direction == "right":
                            if "down" in direzioni:
                                self.direction = "down"
                                changed = True
                            elif "left" in direzioni:
                                self.direction = "left"
                                changed = True
                        if not(changed):
                            self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                    
                    if py <= self.y//16 and px < self.x//16:
                        if self.direction == "up" or self.direction == "down":
                            if "left" in direzioni:
                                self.direction = "left"
                                changed = True
                            elif "up" in direzioni:
                                self.direction = "up"
                                changed = True
                        elif self.direction == "left" or self.direction == "right":
                            if "up" in direzioni:
                                self.direction = "up"
                                changed = True
                            elif "left" in direzioni:
                                self.direction = "left"
                                changed = True
                        if not(changed):
                            self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato 
                else:
                    super().flee(direzioni,map,px,py)
            #elif self.status == "pending":
            #    self.y += self.velox
        self.oldxy = (self.x//16,self.y//16)             
        super().moveghost()
        
class Pinky(Ghost):

    def __init__(self,x,y):
        super().__init__(x,y)
        self.timeforfreedom = 12

    def nextmove(self,px,py,map):
        if self.oldxy!=(self.x//16,self.y//16):
            self.bivio = False
            changed = False
            direzioni = super().way(map) #memorizzo le direzioni possibili
            
            if abs(self.x//16 - px)<=12 and abs(self.y//16 -py)<=12:
                px = 4
                py = 32
            
            if self.status != "pending":
                if not(self.cursed):
                    if self.bivio:
                        if py >= self.y//16 and px>self.x//16:
                            if self.direction == "up" or self.direction == "down":
                                if "right" in direzioni:
                                    self.direction = "right"
                                    changed = True
                                elif "down" in direzioni:
                                    self.direction = "down"
                                    changed = True
                            elif self.direction == "left" or self.direction == "right":
                                if "down" in direzioni:
                                    self.direction = "down"
                                    changed = True
                                elif "right" in direzioni:
                                    self.direction = "right"
                                    changed = True
                            if not(changed):
                                self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                        
                        if py < self.y//16 and px >= self.x//16:
                            if self.direction == "up" or self.direction == "down":
                                if "right" in direzioni:
                                    self.direction = "right"
                                    changed = True
                                elif "up" in direzioni:
                                    self.direction = "up"
                                    changed = True
                            elif self.direction == "left" or self.direction == "right":
                                if "up" in direzioni:
                                    self.direction = "up"
                                    changed = True
                                elif "right" in direzioni:
                                    self.direction = "right"
                                    changed = True
                            if not(changed):
                                self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                                
                        if py > self.y//16 and px <= self.x//16:
                            if self.direction == "up" or self.direction == "down":
                                if "left" in direzioni:
                                    self.direction = "left"
                                    changed = True
                                elif "down" in direzioni:
                                    self.direction = "down"
                                    changed = True
                            elif self.direction == "left" or self.direction == "right":
                                if "down" in direzioni:
                                    self.direction = "down"
                                    changed = True
                                elif "left" in direzioni:
                                    self.direction = "left"
                                    changed = True
                            if not(changed):
                                self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
                        
                        if py <= self.y//16 and px < self.x//16:
                            if self.direction == "up" or self.direction == "down":
                                if "left" in direzioni:
                                    self.direction = "left"
                                    changed = True
                                elif "up" in direzioni:
                                    self.direction = "up"
                                    changed = True
                            elif self.direction == "left" or self.direction == "right":
                                if "up" in direzioni:
                                    self.direction = "up"
                                    changed = True
                                elif "left" in direzioni:
                                    self.direction = "left"
                                    changed = True
                            if not(changed):
                                self.direction = direzioni[0] #vado nella prima direzione che casualmente ho trovato
            
                else:
                    super().flee(direzioni,map,px,py)
            #elif self.status == "pending":
            #    self.y += self.velox
        self.oldxy = (self.x//16,self.y//16)             
        super().moveghost()    
        