#include "header.h"

void clear_file() {
	s.open(italiano, ios::out | ios::binary);
	s.close();
	s.open(english, ios::out | ios::binary);
	s.close();
	s.open(deutsche, ios::out | ios::binary);
	s.close();
	s.open(french, ios::out | ios::binary);
	s.close();
}

int scelta() {
	int scelta = 0;
	do {
		system("cls");
		cout << "inserisci l'operazione che vuoi eseguire: " << endl;
		cout << "1. cancellare tutti i valori nei file\n2. inserire una nuova parola\n3. cercare una traduzione\n";
		cin >> scelta;
	} while (scelta <= 0 || scelta >= 4);
	return scelta;
}

bool continuare() {
	cout << "Continuare? digita 1 se vuoi continuare altrimenti un numero qualsiasi: ";
	int digitato;
	cin >> digitato;
	if (digitato == 1) return true;
	else return false;
}