#include "header.h"

void cerca_traduzione() {
	IT cercato;
	cout << "inserisci la parola che stai cercando: "; cin >> cercato.parola;
	s.open(italiano, ios::in | ios::binary);
	s.seekg(0, ios::end);
	int size = int(s.tellg()) / sizeof(IT);
	s.close();
	int pos = binary_search(italiano, 0, size, cercato);
	if (pos == -1) cout << "la parola cercata non s' presente nel dizionario!" << endl;
	else {
		IT ita; char en[len_w], fr[len_w], de[len_w];
		take_values(pos, ita, en, fr, de);
		cout << "italiano: " << ita.parola << endl;
		cout << "inglese: " << en << endl;
		cout << "francese: " << fr << endl;
		cout << "tedesco: " << de << endl;
	}
}

int binary_search(const char* file, int f, int l, IT cercato) {
	IT c;
	if (l > f) {
		s.open(file, ios::in | ios::binary);
		int mid = f + (l - f) / 2;
		s.seekg(mid * streampos(sizeof(IT)));
		s.read((char*)&c, sizeof(IT));
		if (c == cercato) {
			s.close();
			return mid;
		}
		else if (cercato > c) {
			s.close();
			return binary_search(file, mid + 1, l, cercato);
		}
		else {
			s.close();
			return binary_search(file, f, mid, cercato);
		}
	}

	s.close();
	return -1;
}

void take_values(int n, IT& ita, char en[], char fr[], char de[]) {
	s.open(italiano, ios::in | ios::binary);
	s.seekg(n * streampos(sizeof(IT)));
	s.read((char*)&ita, sizeof(IT));
	s.close();
	s.open(english, ios::in | ios::binary);
	s.seekg(ita.en * streampos(len_w));
	s.read((char*)en, len_w);
	s.close();
	s.open(french, ios::in | ios::binary);
	s.seekg(ita.fr * streampos(len_w));
	s.read((char*)fr, len_w);
	s.close();
	s.open(deutsche, ios::in | ios::binary);
	s.seekg(ita.de * streampos(len_w));
	s.read((char*)de, len_w);
	s.close();
}