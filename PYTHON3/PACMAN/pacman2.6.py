import pygame
import time
from classi25 import *

#30x34



#colors##############################################à
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(0,255,0)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,255)
PURPLE=(255,0,255)
ORANGE=(255,255,0)


#######################################
# immagini

pizzaimgRIGHT = [pygame.image.load("IMAGES/PIZZA/RIGHT/pizza1.png"),pygame.image.load("IMAGES/PIZZA/RIGHT/pizza2.png"),pygame.image.load("IMAGES/PIZZA/RIGHT/pizza3.png"),pygame.image.load("IMAGES/PIZZA/RIGHT/pizza4.png"),pygame.image.load("IMAGES/PIZZA/DOWN/pizza5.png")]
pizzaimgLEFT = [pygame.image.load("IMAGES/PIZZA/LEFT/pizza1.png"),pygame.image.load("IMAGES/PIZZA/LEFT/pizza2.png"),pygame.image.load("IMAGES/PIZZA/LEFT/pizza3.png"),pygame.image.load("IMAGES/PIZZA/LEFT/pizza4.png"),pygame.image.load("IMAGES/PIZZA/LEFT/pizza5.png")]
pizzaimgUP = [pygame.image.load("IMAGES/PIZZA/UP/pizza1.png"),pygame.image.load("IMAGES/PIZZA/UP/pizza2.png"),pygame.image.load("IMAGES/PIZZA/UP/pizza3.png"),pygame.image.load("IMAGES/PIZZA/UP/pizza4.png"),pygame.image.load("IMAGES/PIZZA/UP/pizza5.png")]
pizzaimgDOWN = [pygame.image.load("IMAGES/PIZZA/DOWN/pizza1.png"),pygame.image.load("IMAGES/PIZZA/DOWN/pizza2.png"),pygame.image.load("IMAGES/PIZZA/DOWN/pizza3.png"),pygame.image.load("IMAGES/PIZZA/DOWN/pizza4.png"),pygame.image.load("IMAGES/PIZZA/DOWN/pizza5.png")]
pizzaimgWOMAN = [pygame.image.load("IMAGES/PIZZA/WOMAN/pizza1.png"),pygame.image.load("IMAGES/PIZZA/WOMAN/pizza2.png"),pygame.image.load("IMAGES/PIZZA/WOMAN/pizza3.png"),pygame.image.load("IMAGES/PIZZA/WOMAN/pizza4.png"),pygame.image.load("IMAGES/PIZZA/WOMAN/pizza5.png")]
food1 = pygame.image.load("IMAGES/FOOD/food1-pixilart.png")
food2 = pygame.image.load("IMAGES/FOOD/food2-pixilart.png")

sueimg = {"sueup1":pygame.image.load("IMAGES/SUE/sueup1.png"),"sueup2":pygame.image.load("IMAGES/SUE/sueup2.png"),"suedown1":pygame.image.load("IMAGES/SUE/suedown1.png"),"suedown2":pygame.image.load("IMAGES/SUE/suedown2.png"),"sueleft1":pygame.image.load("IMAGES/SUE/sueleft1.png"),"sueleft2":pygame.image.load("IMAGES/SUE/sueleft2.png"),"sueright1":pygame.image.load("IMAGES/SUE/sueright1.png"),"sueright2":pygame.image.load("IMAGES/SUE/sueright2.png")}
pinkyimg ={"pinkyup1":pygame.image.load("IMAGES/PINKY/pinkyup1.png"),"pinkyup2":pygame.image.load("IMAGES/PINKY/pinkyup2.png"),"pinkydown1":pygame.image.load("IMAGES/PINKY/pinkydown1.png"),"pinkydown2":pygame.image.load("IMAGES/PINKY/pinkydown2.png"),"pinkyleft1":pygame.image.load("IMAGES/PINKY/pinkyleft1.png"),"pinkyleft2":pygame.image.load("IMAGES/PINKY/pinkyleft2.png"),"pinkyright1":pygame.image.load("IMAGES/PINKY/pinkyright1.png"),"pinkyright2":pygame.image.load("IMAGES/PINKY/pinkyright2.png")} 
blinkyimg ={"blinkyup1":pygame.image.load("IMAGES/BLINKY/blinkyup1.png"),"blinkyup2":pygame.image.load("IMAGES/BLINKY/blinkyup2.png"),"blinkydown1":pygame.image.load("IMAGES/BLINKY/blinkydown1.png"),"blinkydown2":pygame.image.load("IMAGES/BLINKY/blinkydown2.png"),"blinkyleft1":pygame.image.load("IMAGES/BLINKY/blinkyleft1.png"),"blinkyleft2":pygame.image.load("IMAGES/BLINKY/blinkyleft2.png"),"blinkyright1":pygame.image.load("IMAGES/BLINKY/blinkyright1.png"),"blinkyright2":pygame.image.load("IMAGES/BLINKY/blinkyright2.png")}
inkyimg = {"inkyup1":pygame.image.load("IMAGES/INKY/inkyup1.png"),"inkyup2":pygame.image.load("IMAGES/INKY/inkyup2.png"),"inkydown1":pygame.image.load("IMAGES/INKY/inkydown1.png"),"inkydown2":pygame.image.load("IMAGES/INKY/inkydown2.png"),"inkyleft1":pygame.image.load("IMAGES/INKY/inkyleft1.png"),"inkyleft2":pygame.image.load("IMAGES/INKY/inkyleft2.png"),"inkyright1":pygame.image.load("IMAGES/INKY/inkyright1.png"),"inkyright2":pygame.image.load("IMAGES/INKY/inkyright2.png")}
cursedimg = {"cursed1": pygame.image.load("IMAGES/CURSED/cursed1.png"),"cursed2": pygame.image.load("IMAGES/CURSED/cursed2.png"),"cursedend1": pygame.image.load("IMAGES/CURSED/cursedend1.png"),"cursedend2": pygame.image.load("IMAGES/CURSED/cursedend2.png")}
gameover = pygame.image.load("IMAGES/gameover.png")
thugpizza = pygame.image.load("IMAGES/PIZZA/thugpizza.png")
#winner = pygame.image.load("IMAGES/win.png")

########################################


pizza = Pizza(14*16,25*16)
sue = Sue(12*16,15*16)  #12*16,15*16
pinky = Pinky (14*16,15*16)#14*16,15*16
inky = Inky (16*16,15*16) #16*16,15*16 in #14*16,11*16 out
blinky = Blinky (14*16,11*16)
##########################################

pygame.init()

win = pygame.display.set_mode((480,544+32))
pygame.display.set_caption("PAC-MAN @HeyJOe")

#################variabili
run=True
looser = False
vel = 5
conta=0
conta2 = 0
SCORE = 0
cursetime = 0 
store = list()
pos = 0
oldt = time.time()
conta_mangiati_liberati = 0

mappa = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,2,2,2,2,2,2,2,2,2,2,2,2,1,0],[0,2,1,1,1,1,2,1,1,1,1,1,2,1,0,0,2,1,1,1,1,1,2,1,1,1,1,2,1,0],[0,3,1,0,0,0,2,1,0,0,0,0,2,1,0,0,2,1,0,0,0,0,2,1,0,0,0,3,1,0],[0,2,1,0,0,0,2,1,0,0,0,0,2,1,0,0,2,1,0,0,0,0,2,1,0,0,0,2,1,0],[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0],[0,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,0],[0,2,1,0,0,0,2,1,0,2,1,0,0,0,0,0,0,0,0,2,1,0,2,1,0,0,0,2,1,0],[0,2,2,2,2,2,2,1,0,2,2,2,2,1,0,0,2,2,2,2,1,0,2,2,2,2,2,2,1,0],[0,1,1,1,1,1,2,1,0,1,1,1,2,1,0,0,2,1,1,1,1,0,2,1,1,1,1,1,1,0],[0,0,0,0,0,0,2,1,0,0,0,0,-2,1,0,0,-2,1,0,0,0,0,2,1,0,0,0,0,0,0],[1,1,1,1,1,0,2,1,0,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,1,0,2,1,0,1,1,1,1,1],[1,1,1,1,1,0,2,1,0,-2,1,1,1,1,1,1,1,1,1,-2,1,0,2,1,0,1,1,1,1,1],[1,1,1,1,1,0,2,1,0,-2,1,0,0,0,4,4,0,0,0,-2,1,0,2,1,0,1,1,1,1,1],[0,0,0,0,0,0,2,1,0,-2,1,0,1,1,1,1,1,1,0,-2,1,0,2,1,0,0,0,0,0,0],[-2,-2,-2,-2,-2,-2,2,-2,-2,-2,1,0,1,1,1,1,1,1,0,-2,-2,-2,2,-2,-2,-2,-2,-2,-2,-2],[1,1,1,1,1,1,2,1,1,-2,1,0,1,1,1,1,1,1,0,-2,1,1,2,1,1,1,1,1,1,1],[0,0,0,0,0,0,2,1,0,-2,1,0,1,1,1,1,1,1,0,-2,1,0,2,1,0,0,0,0,0,0],[1,1,1,1,1,0,2,1,0,-2,1,0,0,0,0,0,0,0,0,-2,1,0,2,1,0,1,1,1,1,1],[1,1,1,1,1,0,2,1,0,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,1,0,2,1,0,1,1,1,1,1],[1,1,1,1,1,0,2,1,0,-2,1,1,1,1,1,1,1,1,1,-2,1,0,2,1,0,1,1,1,1,1],[0,0,0,0,0,0,2,1,0,-2,1,0,0,0,0,0,0,0,0,-2,1,0,2,1,0,0,0,0,0,0],[0,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,2,2,2,2,2,2,2,2,2,2,2,2,1,0],[0,2,1,1,1,1,2,1,1,1,1,1,2,1,0,0,2,1,1,1,1,1,2,1,1,1,1,2,1,0],[0,2,1,0,0,0,2,1,0,0,0,0,2,1,0,0,2,1,0,0,0,0,2,1,0,0,0,2,1,0],[0,3,2,2,1,0,2,2,2,2,2,2,2,-2,-2,-2,2,2,2,2,2,2,2,1,0,2,2,3,1,0],[0,1,1,2,1,0,2,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0,2,1,1,1,0],[0,0,0,2,1,0,2,1,0,2,1,0,0,0,0,0,0,0,0,2,1,0,2,1,0,2,1,0,0,0],[0,2,2,2,2,2,2,1,0,2,2,2,2,1,0,0,2,2,2,2,1,0,2,2,2,2,2,2,1,0],[0,2,1,1,1,1,1,1,0,1,1,1,2,1,0,0,2,1,1,1,1,0,1,1,1,1,1,2,1,0],[0,2,1,0,0,0,0,0,0,0,0,0,2,1,0,0,2,1,0,0,0,0,0,0,0,0,0,2,1,0],[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

################################

########################funzioni
def drawlife():
    for i in range (0,pizza.life,1):
        win.blit(pizzaimgRIGHT[1],(i*32,544))
        
def drawpizza():
    if pizza.direction == "left":      #################################################PIZZA
        if conta<15:
            win.blit(pizzaimgLEFT[conta//3],(pizza.x,pizza.y))
        else:
            win.blit(pizzaimgLEFT[(conta-15)//3],(pizza.x,pizza.y))
    if pizza.direction == "right":
        if conta<15:
            win.blit(pizzaimgRIGHT[conta//3],(pizza.x,pizza.y))
        else:
            win.blit(pizzaimgRIGHT[(conta-15)//3],(pizza.x,pizza.y))
    
    if pizza.direction == "up":
        if conta<15:
            win.blit(pizzaimgUP[conta//3],(pizza.x,pizza.y))
        else:
            win.blit(pizzaimgUP[(conta-15)//3],(pizza.x,pizza.y))
    
    if pizza.direction == "down":
        if conta<15:
            win.blit(pizzaimgDOWN[conta//3],(pizza.x,pizza.y))
        else:
            win.blit(pizzaimgDOWN[(conta-15)//3],(pizza.x,pizza.y))

def drawsue():
    if sue.direction == "down" and not(sue.cursed):            ################################################ SUE
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(sueimg["suedown1"],(sue.x,sue.y))
        else:
            win.blit(sueimg["suedown2"],(sue.x,sue.y))
    if sue.direction == "up" and not(sue.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(sueimg["sueup1"],(sue.x,sue.y))
        else:
            win.blit(sueimg["sueup2"],(sue.x,sue.y))
    if sue.direction == "left" and not(sue.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(sueimg["sueleft1"],(sue.x,sue.y))
        else:
            win.blit(sueimg["sueleft2"],(sue.x,sue.y))
    if sue.direction == "right" and not(sue.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(sueimg["sueright1"],(sue.x,sue.y))
        else:
            win.blit(sueimg["sueright2"],(sue.x,sue.y))
    if (sue.cursed):
        if time.time()-cursetime < 2.3:
            if conta//5==0 or conta//5==2 or conta//5==4:
                win.blit(cursedimg["cursed1"],(sue.x,sue.y))
            else:
                win.blit(cursedimg["cursed2"],(sue.x,sue.y))
        if time.time()-cursetime >= 2.3:
            if conta//3==0 or conta//3==2 or conta//3==4:
                win.blit(cursedimg["cursed1"],(sue.x,sue.y))
            elif conta//3==1 or conta//3==3 or conta//3==5:
                win.blit(cursedimg["cursed2"],(sue.x,sue.y))
            elif conta//3==6 or conta//3==8 or conta//3==10:
                win.blit(cursedimg["cursedend1"],(sue.x,sue.y))
            elif conta//3==7 or conta//3==9:
                win.blit(cursedimg["cursedend2"],(sue.x,sue.y))

def drawblinky():
    if blinky.direction == "down" and not(blinky.cursed):            ################################################ blinky
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(blinkyimg["blinkydown1"],(blinky.x,blinky.y))
        else:
            win.blit(blinkyimg["blinkydown2"],(blinky.x,blinky.y))
    if blinky.direction  ==  "up" and not(blinky.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(blinkyimg["blinkyup1"],(blinky.x,blinky.y))
        else:
            win.blit(blinkyimg["blinkyup2"],(blinky.x,blinky.y))
    if blinky.direction  ==  "left" and not(blinky.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(blinkyimg["blinkyleft1"],(blinky.x,blinky.y))
        else:
            win.blit(blinkyimg["blinkyleft2"],(blinky.x,blinky.y))
    if blinky.direction  ==  "right" and not(blinky.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(blinkyimg["blinkyright1"],(blinky.x,blinky.y))
        else:
            win.blit(blinkyimg["blinkyright2"],(blinky.x,blinky.y))

    if (blinky.cursed):
        if time.time()-cursetime < 2.3:
            if conta//5==0 or conta//5==2 or conta//5==4:
                win.blit(cursedimg["cursed1"],(blinky.x,blinky.y))
            else:
                win.blit(cursedimg["cursed2"],(blinky.x,blinky.y))
        if time.time()-cursetime >= 2.3:
            if conta//3==0 or conta//3==2 or conta//3==4:
                win.blit(cursedimg["cursed1"],(blinky.x,blinky.y))
            elif conta//3==1 or conta//3==3 or conta//3==5:
                win.blit(cursedimg["cursed2"],(blinky.x,blinky.y))
            elif conta//3==6 or conta//3==8 or conta//3==10:
                win.blit(cursedimg["cursedend1"],(blinky.x,blinky.y))
            elif conta//3==7 or conta//3==9:
                win.blit(cursedimg["cursedend2"],(blinky.x,blinky.y))

def drawinky():
    if inky.direction  ==  "down" and not(inky.cursed):            ################################################ inky
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(inkyimg["inkydown1"],(inky.x,inky.y))
        else:
            win.blit(inkyimg["inkydown2"],(inky.x,inky.y))
    if inky.direction  ==  "up" and not(inky.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(inkyimg["inkyup1"],(inky.x,inky.y))
        else:
            win.blit(inkyimg["inkyup2"],(inky.x,inky.y))
    if inky.direction  ==  "left" and not(inky.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(inkyimg["inkyleft1"],(inky.x,inky.y))
        else:
            win.blit(inkyimg["inkyleft2"],(inky.x,inky.y))
    if inky.direction  ==  "right" and not(inky.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(inkyimg["inkyright1"],(inky.x,inky.y))
        else:
            win.blit(inkyimg["inkyright2"],(inky.x,inky.y))
    
    if (inky.cursed):
        if time.time()-cursetime < 2.3:
            if conta//5==0 or conta//5==2 or conta//5==4:
                win.blit(cursedimg["cursed1"],(inky.x,inky.y))
            else:
                win.blit(cursedimg["cursed2"],(inky.x,inky.y))
        if time.time()-cursetime >= 2.3:
            if conta//3==0 or conta//3==2 or conta//3==4:
                win.blit(cursedimg["cursed1"],(inky.x,inky.y))
            elif conta//3==1 or conta//3==3 or conta//3==5:
                win.blit(cursedimg["cursed2"],(inky.x,inky.y))
            elif conta//3==6 or conta//3==8 or conta//3==10:
                win.blit(cursedimg["cursedend1"],(inky.x,inky.y))
            elif conta//3==7 or conta//3==9:
                win.blit(cursedimg["cursedend2"],(inky.x,inky.y))

def drawpinky():
    if pinky.direction  ==  "down" and not(pinky.cursed):            ################################################ pinky
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(pinkyimg["pinkydown1"],(pinky.x,pinky.y))
        else:
            win.blit(pinkyimg["pinkydown2"],(pinky.x,pinky.y))
    if pinky.direction  ==  "up" and not(pinky.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(pinkyimg["pinkyup1"],(pinky.x,pinky.y))
        else:
            win.blit(pinkyimg["pinkyup2"],(pinky.x,pinky.y))
    if pinky.direction  ==  "left" and not(pinky.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(pinkyimg["pinkyleft1"],(pinky.x,pinky.y))
        else:
            win.blit(pinkyimg["pinkyleft2"],(pinky.x,pinky.y))
    if pinky.direction  ==  "right" and not(pinky.cursed):
        if conta//5==0 or conta//5==2 or conta//5==4:
            win.blit(pinkyimg["pinkyright1"],(pinky.x,pinky.y))
        else:
            win.blit(pinkyimg["pinkyright2"],(pinky.x,pinky.y))

    if (pinky.cursed):
        if time.time()-cursetime < 2.3:
            if conta//5==0 or conta//5==2 or conta//5==4:
                win.blit(cursedimg["cursed1"],(pinky.x,pinky.y))
            else:
                win.blit(cursedimg["cursed2"],(pinky.x,pinky.y))
        if time.time()-cursetime >= 2.3:
            if conta//3==0 or conta//3==2 or conta//3==4:
                win.blit(cursedimg["cursed1"],(pinky.x,pinky.y))
            elif conta//3==1 or conta//3==3 or conta//3==5:
                win.blit(cursedimg["cursed2"],(pinky.x,pinky.y))
            elif conta//3==6 or conta//3==8 or conta//3==10:
                win.blit(cursedimg["cursedend1"],(pinky.x,pinky.y))
            elif conta//3==7 or conta//3==9:
                win.blit(cursedimg["cursedend2"],(pinky.x,pinky.y))
    
def startagain():
    pizza.x = 14*16
    pizza.y = 25*16
    sue.x = 12*16
    sue.y = 15*16
    sue.t = time.time()
    sue.status = "pending"
    pinky.x = 14*16
    pinky.y = 15*16
    pinky.t = time.time()
    pinky.status = "pending"
    inky.x = 16*16
    inky.y = 15*16
    inky.t = time.time()
    inky.status = "pending"
    blinky.x = 14*16
    blinky.y = 11*16
    blinky.t = time.time()
    blinky.status = "pending"
    blinky.not_up_right = True
    sue.out = False
    inky.out = False
    blinky.out = False
    pinky.out = False
    
def checkcollision():
    global pos
    global looser
    global store
    global SCORE
    global conta_mangiati_liberati
    global oldt

    stringa_display = "400"
    FONT2 = pygame.font.SysFont("Times New Roman", 24, bold = True)
    TEXT2 = FONT2.render(stringa_display, True, RED) #crea superficie con il testo

    if sue.collision(pizza.x,pizza.y) and not(sue.cursed):
        pizza.life -= 1
        startagain()
        time.sleep(1)
        looser = True

    if inky.collision(pizza.x,pizza.y) and not(inky.cursed):
        pizza.life -= 1
        startagain()
        time.sleep(1)
        looser = True

    if pinky.collision(pizza.x,pizza.y) and not(pinky.cursed):
        pizza.life -= 1
        startagain()
        time.sleep(1)
        looser = True

    if blinky.collision(pizza.x,pizza.y) and not(blinky.cursed):
        pizza.life -= 1
        startagain()
        time.sleep(1)
        looser = True

    if sue.cursed and sue.collision(pizza.x,pizza.y):
        SCORE += 400
        sue.status = "pending"
        sue.x = 12*16 #12
        sue.y = 15*16
        sue.t = time.time()
        sue.direction = "up"
        store.append(sue)
        if conta_mangiati_liberati == 0:
            oldt = time.time()
        conta_mangiati_liberati += 1
        #win.blit(TEXT2,(12*16,15*16))
        #time.sleep(0.5)
        

    if inky.cursed and inky.collision(pizza.x,pizza.y):
        SCORE += 400
        inky.status = "pending"
        inky.x = 16*16
        inky.y = 15*16
        inky.t = time.time()
        inky.direction = "up"
        store.append(inky)
        if conta_mangiati_liberati == 0:
            oldt = time.time()
        conta_mangiati_liberati += 1
        #win.blit(TEXT2,(12*16,15*16))
        #time.sleep(0.5)

    if blinky.cursed and blinky.collision(pizza.x,pizza.y):
        SCORE += 400
        blinky.status = "pending"
        blinky.x = 14*16
        blinky.y = 15*16
        blinky.t = time.time()
        blinky.direction = "up"
        store.append(blinky)
        if conta_mangiati_liberati == 0:
            oldt = time.time()
        conta_mangiati_liberati += 1
        #win.blit(TEXT2,(12*16,15*16))
        #time.sleep(0.5)

    if pinky.cursed and pinky.collision(pizza.x,pizza.y):
        SCORE += 400
        pinky.status = "pending"
        pinky.x = 14*16
        pinky.y = 15*16
        pinky.t = time.time()
        pinky.direction = "up"
        store.append(pinky)
        if conta_mangiati_liberati == 0:
            oldt = time.time()
        conta_mangiati_liberati += 1
        #win.blit(TEXT2,(0*16,0*16))
        #time.sleep(0.5)
        
def liberate():
    global conta_mangiati_liberati
    global pos
    global store
    global oldt
    a = time.time()
    #if pinky.out == False or inky.out == False or blinky.out == False or sue.out == False:
    if pinky.status == "pending" and not(pinky.out):
        if a - pinky.t >= pinky.timeforfreedom :       #arancione
            pinky.x = 14*16
            pinky.y = 11*16
            pinky.direction = "left"
            pinky.out = True
    if sue.status == "pending" and not(sue.out):
        if a - sue.t >= sue.timeforfreedom:     #rosa
            sue.x = 14*16
            sue.y = 11*16
            sue.direction = "right"
            sue.out = True
    if blinky.status == "pending" and not(blinky.out):
        if a - blinky.t >= blinky.timeforfreedom:
            blinky.x = 14*16
            blinky.y = 11*16
            blinky.direction = "right"
            blinky.out = True
    if inky.status == "pending" and not(inky.out):
        if a - inky.t >= inky.timeforfreedom:     #blu
            inky.x = 14*16
            inky.y = 11*16
            inky.direction = "left"
            inky.out = True
    
    """
    """
    #print(type(store))
    #print(time.time()-oldt)
    #print(len(store))
    if  time.time() - oldt >= 4 and len(store) > pos :
        #print ("here")
        store[pos].x = 14*16
        store[pos].y = 11*16
        store[pos].direction = "left"
        oldt = time.time()
        conta_mangiati_liberati -= 1
        pos += 1
    
#################################################

def draw():
    picaini = 0
    global conta
    global looser
    global run
    win.fill(BLACK)  
    n=-1
    m=-1
    for submappa in mappa:
        n+=1
        m=-1
        #print(type(submappa))
        for g in submappa:
            m+=1
            if g == 0:
                pygame.draw.rect(win,BLUE,[m*16,n*16,16,16])
            if g == 2:
                win.blit(food1,(m*16,n*16))
                picaini += 1
            if g == 3:
                win.blit(food2,(m*16,n*16))
                picaini += 1
            if g == 4:
                pygame.draw.rect(win,WHITE,[m*16,n*16+6,16,6])
            if g == -2:
                pass

    #picaini = 0 #DA ELIMINARE
    #print(picaini)
    if picaini == 0:
        run = False
        looser = False

    drawpizza()
    drawsue()
    drawpinky()
    drawblinky()
    drawinky()
    drawlife()

    global SCORE
    stringa_punteggio = "SCORE: "+str(SCORE)
    FONT = pygame.font.SysFont("Times New Roman", 24)
    TEXT = FONT.render(stringa_punteggio, True, WHITE) #crea superficie con il testo
    win.blit(TEXT,(300,544+1)) #disegna score #480+16,544

    #pygame.draw.rect(win,YELLOW,[12*16,14*16,16*6,16*4])

    global conta2
    conta+=1 
    if conta==30:
        conta=0
        conta2+=1
        if conta2==4:
            conta2=0

def pizzaMOVING():
    global SCORE
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and (pizza.x - vel)//16 < 0:
        pizza.direction = "left"
        pizza.x = 480-32
    if key[pygame.K_LEFT] and (mappa[pizza.y//16][(pizza.x-8)//16]==2 or mappa[pizza.y//16][(pizza.x-8)//16]==-2 or mappa[pizza.y//16][(pizza.x-8)//16]==3):# and mappa[pizza.y//16][(pizza.x-8)//16]!=1:
        pizza.direction = "left"
        if mappa[pizza.y//16][(pizza.x-16)//16] ==  -2:
            pizza.x-=int(vel+vel*0.2)
        else:
            pizza.x-=vel
    if key[pygame.K_RIGHT] and pizza.x + vel>=480-16:
        pizza.direction = "right"
        pizza.x=0
    if key[pygame.K_RIGHT] and (mappa[pizza.y//16][(pizza.x+16)//16]==2 or mappa[pizza.y//16][(pizza.x+16)//16]==-2 or mappa[pizza.y//16][(pizza.x+16)//16]==3):
        pizza.direction = "right"
        if mappa[pizza.y//16][(pizza.x+16)//16] ==  -2:
            pizza.x+=int(vel+vel*0.2)
        else:
            pizza.x+=vel
    if key[pygame.K_UP] and (mappa[(pizza.y-8)//16][pizza.x//16]==2 or mappa[(pizza.y-8)//16][pizza.x//16]==-2 or mappa[(pizza.y-8)//16][pizza.x//16]==3):
        pizza.direction = "up"
        if mappa[(pizza.y-16)//16][pizza.x//16] == -2:
            pizza.y-=int(vel+vel*0.2)
        else:
            pizza.y-=vel
    if key[pygame.K_DOWN] and (mappa[(pizza.y+16)//16][pizza.x//16]==2 or mappa[(pizza.y+16)//16][pizza.x//16]==-2 or mappa[(pizza.y+16)//16][pizza.x//16]==3):
        pizza.direction = "down"
        if mappa[(pizza.y+16)//16][pizza.x//16] ==  -2:
            pizza.y+=int(vel+vel*0.2)
        else:
            pizza.y+=vel
    if mappa[(pizza.y)//16][pizza.x//16] == 2:
        SCORE+=100
        mappa[(pizza.y)//16][pizza.x//16] = -2

    if (pizza.direction == "left" or pizza.direction == "right"):
        pizza.y=(pizza.y//16)*16 ##corregge la posizione y

    if pizza.direction == "up" or pizza.direction == "down":
        pizza.x=(pizza.x//16)*16
    
##################################


while run:
    pygame.time.delay(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            looser = True

    liberate()

    pizzaMOVING() #utiliza tutte le variabili

    if mappa[pizza.y//16][pizza.x//16] == 3:    #li importa a curse
        mappa[pizza.y//16][pizza.x//16] = -2
        cursetime = time.time()
        sue.cursed = True
        inky.cursed = True
        blinky.cursed = True
        pinky.cursed = True
    
    if cursetime != 0:      #libera i fantasmi da curse
        if (time.time())-(cursetime) >= 5:
            cursetime = 0
            sue.cursed = False
            inky.cursed = False
            blinky.cursed = False
            pinky.cursed = False

    blinky.nextmove(pizza.x//16,pizza.y//16,mappa)
    inky.nextmove(pizza.x//16,pizza.y//16,mappa,pizza.direction,blinky.status)
    sue.nextmove(pizza.x//16,pizza.y//16,mappa,pizza.direction)
    pinky.nextmove(pizza.x//16,pizza.y//16,mappa)
    
    checkcollision()

    sue.setstatus()
    inky.setstatus()
    pinky.setstatus()
    blinky.setstatus()

    

    draw()

    if pizza.life == 0:
        run = False
    pygame.display.update()

#pygame.display.update()
    if looser  and not(run):
        """
        stringa_display = "TOTAL SCORE : " + str(SCORE)
        FONT = pygame.font.SysFont("Times New Roman", 32, bold = True)
        TEXT3 = FONT.render(stringa_display, True, WHITE) #crea superficie con il testo
        """
        """
        win.fill(BLACK)
        
        win.blit(TEXT3,(80,400))
        pygame.display.update()
        """
        for k in range (0,SCORE+100,100):
            win.fill(BLACK)
            win.blit(gameover,(100,100))
            stringa_punteggio = "SCORE: "+str(k)
            FONT = pygame.font.SysFont("Times New Roman", 40)
            TEXT = FONT.render(stringa_punteggio, True, WHITE) #crea superficie con il testo
            win.blit(TEXT,(100,400)) #disegna score #480+16,544
            pygame.display.update()
        #time.sleep(3)

    elif not(looser) and not(run):
        stringa_display = "TOTAL SCORE " + str(SCORE)
        FONT = pygame.font.SysFont("Times New Roman", 32, bold = True)
        TEXT3 = FONT.render(stringa_display, True, BLUE) #crea superficie con il testo
        win.fill(BLACK)
        #win.blit(gameover,(110,100))
        win.blit(TEXT3,(100,400))
        pygame.display.update()

        #animation
        pizzawoman = Pizza(400,200)
        pizza.x = 60
        pizza.y = 200
        pizza.direction = "right"
        for h in range (1000,4000):
            win.fill(BLACK)
            if (h-1000)%100 == 0:
                pizzawoman.x -= 5
                pizza.x += 5
            let = str(h)
            n = int(let[1])
            if n>=5:
                n = -(n-5)
            win.blit(pizzaimgRIGHT[n],(pizza.x,pizza.y))
            win.blit(pizzaimgWOMAN[n],(pizzawoman.x,pizzawoman.y))

            pygame.display.update()
        
        for n in range (0,3):
            for a in range (7,0,-1):
                pygame.time.delay(30)
                win.fill(BLACK)
                pizza.y -= int((a**2)*0.5)
                pizzawoman.y -= int((a**2)*0.5)
                win.blit(pizzaimgRIGHT[2],(pizza.x,pizza.y))
                win.blit(pizzaimgWOMAN[2],(pizzawoman.x,pizzawoman.y))
                pygame.display.update()
            for a in range (7,0,-1):
                pygame.time.delay(30)
                win.fill(BLACK)
                pizza.y += int((a**2)*0.5)
                pizzawoman.y += int((a**2)*0.5)
                win.blit(pizzaimgRIGHT[2],(pizza.x,pizza.y))
                win.blit(pizzaimgWOMAN[2],(pizzawoman.x,pizzawoman.y))
                pygame.display.update()

        for h in range (1000,6700):
            win.fill(BLACK)
            if (h-1000)%100 == 0:
                pizzawoman.x -= 7
                pizza.x -= 7
            let = str(h)
            n = int(let[1])
            if n>=5:
                n = -(n-5)
            win.blit(pizzaimgLEFT[n],(pizza.x,pizza.y))
            win.blit(pizzaimgWOMAN[n],(pizzawoman.x,pizzawoman.y))

            pygame.display.update()

        sue.x = 31*16
        sue.y = 200
        sue.direction = "left"
        blinky.x = 33*16 +2
        blinky.y = 200
        blinky.direction = "left"
        pinky.x = 35*16 +2
        pinky.direction = "left"
        pinky.y = 200
        inky.direction = "left"
        inky.x = 37*16 +2
        inky.y = 200
        for u in range (0,180):
            pygame.time.delay(20)
            win.fill(BLACK)
            if u%4 == 0 or u%4 == 2:
                win.blit(sueimg["sueleft1"],(sue.x,sue.y))
                win.blit(inkyimg["inkyleft1"],(inky.x,inky.y))
                win.blit(blinkyimg["blinkyleft1"],(blinky.x,blinky.y))
                win.blit(pinkyimg["pinkyleft1"],(pinky.x,pinky.y))
                
            else:
                win.blit(sueimg["sueleft2"],(sue.x,sue.y))
                win.blit(inkyimg["inkyleft2"],(inky.x,inky.y))
                win.blit(blinkyimg["blinkyleft2"],(blinky.x,blinky.y))
                win.blit(pinkyimg["pinkyleft2"],(pinky.x,pinky.y))

            if u%2 == 0:
                sue.x -= 7
                inky.x -= 7
                pinky.x -= 7
                blinky.x -= 7
            pygame.display.update()

        #SCORE = 10000
        for k in range (0,SCORE+100,100):
            win.fill(BLACK)
            win.blit(thugpizza,(120,90))
            stringa_punteggio = "SCORE: "+str(k)
            FONT = pygame.font.SysFont("Times New Roman", 40)
            TEXT = FONT.render(stringa_punteggio, True, WHITE) #crea superficie con il testo
            win.blit(TEXT,(120,400)) #disegna score #480+16,544
            pygame.display.update()

        
    
    if not(run):        #anti crash
        while not(run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=True
        run = False



pygame.quit()
