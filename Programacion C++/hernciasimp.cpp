#include <iostream>
 
using namespace std;
 
class Texto {
  private:
     std::string texto;
  public:
     Texto(std::string t="Hola Mundo"){
        texto = t;
     };
     std::string getTexto() const {return texto;}
     void setTexto(std::string t){
        texto = t;
     }
};
 
class TextoMayus:public Texto { };
 
class TextoMinus:public Texto {
    private:
     std::string texto;
  public:
     TextoMinus(std::string t="hola mundo"):Texto(t){
         texto=t;
     }
     std::string getTextoMin() const {return texto;}
};
 
int main(){
    TextoMinus tminus;
    cout << "Texto en Minusculas" << endl;
    cout << "Texto: " << tminus.getTextoMin() << endl;
    tminus.setTexto("Hola Mundo");
    cout << "After: " << tminus.getTexto() << endl;
}