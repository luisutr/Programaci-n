#include <iostream>
 
using namespace std;
 
class Animal {
  public:
       void caminar() {
           cout << "Caminando el Animal" << endl;
       }
};
 
class Mamifero{
  public:
       void mamar() {
           cout << "Mamando el Mamifero" << endl;
       }    
};
 
class Perro:public Animal, public Mamifero { };
 
int main(){
    Perro dog;
    dog.caminar();
    dog.mamar();
}