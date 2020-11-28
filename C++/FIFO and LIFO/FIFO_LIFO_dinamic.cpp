#include <iostream>

//using namespace std;
template <class F>
struct Element {
	F value;
	Element<F>* pointer;
};

template <class T>
class Coda {
	public:
		Coda() { 
			last = NULL; 
			first = NULL;
			elementi = 0;
		}
		int size() { return elementi; }
	protected:
		Element <T>* first;
		Element <T>* last;
		int elementi;
};

template <class V>
class LIFO : public Coda <V>{
	public:
		void push_back(V new_element) {
			Coda<V>::elementi++;
			Element<V>* nuovo = new Element<V>();
			if (nuovo == NULL)return;
			nuovo->value = new_element;
			nuovo->pointer = Coda<V>::last;
			Coda<V>::last = nuovo;
			if (Coda<V>::first == NULL) Coda<V>::first = Coda<V>::last;
		}
		void print() {
			std::cout << "elementi: " << Coda<V>::elementi << std::endl;
			for (Element<V>* k = Coda<V>::last; k ->pointer != NULL; k = k->pointer) {
				std::cout << k->value << " ";
			}
			std::cout << Coda<V>::first->value<< std::endl;
		}
		V pop_back() {
			if (Coda<V>::elementi == 0) return 0;
			V valore_pop = (Coda<V>::last)->value;
			Element<V>* to_delete = Coda<V>::last;
			Coda<V>::last = (Coda<V>::last)->pointer;
			delete to_delete;
			Coda<V>::elementi--;
			return valore_pop;
		}
};

template <class G>
class FIFO : public Coda<G> {
	public:
		void push_back(G new_element) {
			Element<G>* nuovo = new Element<G>();
			if (nuovo == NULL)return;
			nuovo->value = new_element;
			nuovo->pointer = NULL;
			if (Coda<G>::elementi == 0) {
				Coda<G>::first = nuovo;
				Coda<G>::last = nuovo;
			}
			else {
				(Coda<G>::last)->pointer = nuovo;
				Coda<G>::last = nuovo;
			}
			Coda<G>::elementi++;
		}


		G pop_front() {
			if (Coda<G>::elementi == 0) return 0;
			G element = (Coda<G>::first)->value;
			Element<G>* to_delete = Coda<G>::first;
			Coda<G>::first = (Coda<G>::first)->pointer;
			delete to_delete;
			Coda<G>::elementi--;
			return element;
		}
		void print() {
			std::cout << "elementi: " << Coda<G>::elementi << std::endl;
			for (Element<G>* k = Coda<G>::first; k->pointer != NULL; k = k->pointer) {
				std::cout << k->value << " ";
			}
			std::cout << Coda<G>::last->value << std::endl;
		}
};

using namespace std;
int main() {
	FIFO <int> fifo;
	fifo.push_back(1);
	fifo.push_back(2);
	fifo.push_back(3);
	fifo.push_back(4);
	cout << "-------------------------------------FIFO-------------------------------------" << endl;
	fifo.print();
	cout << "pop_front(): " << fifo.pop_front() << endl;
	fifo.print();
	cout << "pop_front(): " << fifo.pop_front() << endl;
	fifo.print();
	cout << "pop_front(): " << fifo.pop_front() << endl;
	fifo.print();
	
	cout << endl << "-------------------------------------LIFO-------------------------------------" << endl;
	LIFO <char> lifo;
	lifo.push_back(65);
	lifo.push_back(66);
	lifo.push_back(67);
	lifo.push_back(68);
	lifo.print();
	cout << "pop_back(): " << lifo.pop_back() << endl;
	lifo.print();

	return 0;
}