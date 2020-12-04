#include <iostream>
#include <conio.h>
#include <time.h>
#include <Windows.h>
#include <stdlib.h>
#include <list>
#define game_y 40
#define game_x 40

int player_score = 0;

void  gotoxy(int x, int  y) {
    COORD CursorPos = {(SHORT) x, (SHORT)y };
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleCursorPosition(hConsole, CursorPos);
}

void setcolor(const char* color) {
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    int n = 0;
    if (color == "nero") n = 0;
    else if (color == "green")		 n = 2 * 16 + 2;
    else if (color == "border")	     n = 15 * 16 + 15;
    else if (color == "snake")		 n = 12 * 16 + 12;
    else if (color == "snake head")  n = 4 * 16 + 4;
    else if (color == "kiwi")        n = 0 * 16 + 10;
    else if (color == "text")        n = 0 * 16 + 15;
    SetConsoleTextAttribute(hConsole, n);
}

struct Coord {
    int x, y;
    Coord(int x, int y) : x(x), y(y) {}
    Coord() { x = 0; y = 0;}
    void print() const{
        gotoxy(100, 100);
        std::cout << 'x: ' << x << ' y:' << y << std::endl;
    }
};

bool operator == (Coord a, Coord b) {
    if (a.x == b.x && a.y == b.y) return true;
    else return false;
}

class fruit {
    public:
        Coord coord;
        
        bool check_if_eaten(Coord snake_head) {
            if (snake_head == coord)return true;
            else return false;
        }
        Coord new_position(std::list<Coord>& list) {
            srand(unsigned int(time(NULL)));
            do{
                coord.x = (rand() % (game_x-2)) * 2 + 2;
                coord.y = rand() % (game_y-2) + 1;
            } while (check_if_is_snake_position(list));
            
            int type_fruit = 0;//= rand() % 1;
            gotoxy(coord.x, coord.y);
            switch (type_fruit) {   //212 ananas //211 kiwi
                case 0: setcolor("kiwi"); std::cout << char(153) << char(153); break;
            }
            return coord;
        }
    private:
        bool check_if_is_snake_position(std::list<Coord>& list) {
            for (auto& i : list) {
                if (i == coord)return true;
            }
            return false;
        }
};

using namespace std;
