#include "Snake_header.h"

void move_head(Coord next_coord, list<Coord>& list, char d) {
	gotoxy(list.back().x, list.back().y);
	setcolor("snake");
	std::cout << "00";
	list.push_back(next_coord);
	gotoxy(list.back().x, list.back().y);
	setcolor("snake head");
	cout << "11";
}

void move_tail(list<Coord>& list) {
	Coord b = list.front();
	list.pop_front();
	gotoxy(b.x, b.y);
	setcolor("green");
	cout << "  ";
}

bool check_collision(Coord a,list<Coord>& list) {                            
	if (a.x < 2 || a.x > (game_x-2)*2 || a.y < 0 || a.y > game_y-2) return true;
	else {
		int k = 1;
		for (auto& i : list) {
			if (a == i && !(k == list.size())) return true;
			k++;
		}
	}
	return false;
}

void draw_begin_table() {
	for (int i = 0; i < game_y; i++){
		for (int g = 0; g < game_x; g++) {
			if (i == 0 || i == game_y - 1 || g == 0 || g == game_x-1) {
				setcolor("border");
				std:: cout << "44";
			}
			else {
				setcolor("green");
				std::cout << "99";
			}
		}
	std:: cout << endl;
	}
}

int main() {
	list <Coord> snake;
	fruit fruit;
	system("pause");
	system("cls");
	snake.push_back({ 2,1 });
	snake.push_back({ 2,2 });
	snake.push_back({ 2,3 });
	char direction = 's';
	char old_direction = 'w';
	bool life = true;
	Coord a; //takes differents values

	draw_begin_table();
	fruit.new_position(snake);

	while (life) {
		int key;
		if (_kbhit())
		{
			key = _getch();
			if (key == 224) {
				key = _getch();
				switch (key) {
					case 72: if (old_direction != 's')direction = 'w'; break;
					case 75: if (old_direction != 'd')direction = 'a'; break;
					case 80: if (old_direction != 'w')direction = 's'; break;
					case 77: if (old_direction != 'a')direction = 'd'; break;
					default: direction = '\0';
				}
			}
		}
		a = snake.back(); //head
		switch (direction) {
			case 'w': a.y--; break;
			case 's': a.y++; break;
			case 'a': a.x -= 2; break;
			case 'd': a.x += 2; break;			
		}
		move_head(a,snake,direction);
		if (!fruit.check_if_eaten(snake.back()))move_tail(snake);
		else fruit.new_position(snake);
		life = !check_collision(snake.back(), snake);
		old_direction = direction;
		Sleep(100);
	}

	system("cls");
	setcolor("text");
	cout << "YOUR SCORE: "<<player_score << endl;


	return 0;
}