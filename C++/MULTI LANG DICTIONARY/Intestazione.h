#pragma once
#include <iostream>
#include <string.h>
#include <fstream>
#include <stdlib.h>

#define len_w 100

using namespace std;

struct IT {
	char parola[len_w];
	int en, de, fr;
	bool operator > (IT a) {
		if (strcmp(parola, a.parola) > 0)return true;
		else return false;
	}
	bool operator == (IT a) {
		if (strcmp(parola, a.parola) == 0)return true;
		else return false;
	}
	void _init_() {
		cout << "inserisci la parola in italiano: "; cin >> parola;
		en = 0; de = 0; fr = 0;
	}
};

static const char* italiano = "ita.bin"; //può essere cambiato il valore perchè costante è l'indirizzo non il contenuto (altrimenti const char* const)
static const char* english = "eng.bin";
static const char* deutsche = "de.bin";
static const char* french = "fr.bin";

static fstream s;


void nuova_parola();
int put_in_file(const char* file, char w[]);
int search_pos_ita(const char* file, int n, IT searched_word);
void cerca_traduzione();
int binary_search(const char* file, int f, int l, IT cercato);
void take_values(int n,IT& ita,char en[],char fr[],char de[]);
void clear_file();
bool continuare();
int scelta();




