#include "header.h"

int main(){
	do {
		int s = scelta();
		int k;
		switch (s)
		{
		case 1:
			cout << "sei sicuro di voler eliminare il contenuto dei file?: digita 1 per confermare, altrimenti un tasto qualsiasi: ";
			cin >> k;
			if (k == 1) clear_file();
			else cout << "operazione annullata\n";
			break;
		case 2:
			new_word();
			break;
		case 3:
			cerca_traduzione();
		}
	}
	while (continuare());

	return 0;
}


