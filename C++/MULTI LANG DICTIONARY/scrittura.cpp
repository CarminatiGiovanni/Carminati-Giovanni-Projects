#include "Intestazione.h"

void nuova_parola() {
	char p_en[len_w];
	char p_de[len_w];
	char p_fr[len_w];
	IT p_ita;
	p_ita._init_();
	cout << "inserisci parola in inglese: "; cin >> p_en;
	cout << "inserisci parola in francese: "; cin >> p_fr;
	cout << "inserisci parola in tedesco: "; cin >> p_de;
	p_ita.en = put_in_file(english, p_en);
	p_ita.fr = put_in_file(french, p_fr);
	p_ita.de = put_in_file(deutsche, p_de);
	s.open(italiano, ios::in | ios::binary);
	s.seekp(0, ios::end);
	int file_elements = int(s.tellg()) / sizeof(IT);
	s.close();
	int pos = search_pos_ita(italiano, file_elements, p_ita);
	s.open(italiano, ios::out | ios::in | ios::binary);
	IT scambio;
	for (int i = file_elements; i > pos; i--) { //scala tutti i valori
		s.seekg(((long long int)i - 1) * sizeof(IT));
		s.read((char*)&scambio, sizeof(IT));
		s.seekp(i * streampos(sizeof(IT)));
		s.write((char*)&scambio, sizeof(IT));
	}
	s.seekp(pos * streampos(sizeof(IT)));
	s.write((char*)&p_ita, sizeof(IT));
	s.close();
}

int search_pos_ita(const char* file, int n, IT searched_word)
{
	IT read;
	int pos = 0;
	bool find = false;
	s.open(file, ios::in | ios::binary);
	while (!find && pos < n) {
		s.seekg(pos * streampos(sizeof(IT)));
		s.read((char*)&read, sizeof(IT));
		if (read > searched_word) find = true;
		else pos++;
	}
	s.close();
	return pos;
}

int put_in_file(const char* file, char w[]) {
	s.open(file, ios::app | ios::binary);
	s.seekp(0, ios::end);
	int n_elementi = int(s.tellp()) / len_w;
	s.write((char*)w, len_w);
	s.close();
	return n_elementi;
}