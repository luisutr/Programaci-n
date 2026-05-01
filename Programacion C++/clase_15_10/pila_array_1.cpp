#include <iostream>

enum {MAX = 10};

class Coordenada
{
public:

  Coordenada()
  {
      x_ = 0;
      y_ = 0;
  }

  Coordenada(float ix, float iy)
  {
      x_ = ix;
      y_ = iy;
  }

  ~Coordenada()
  {
    std::cout<<"DESTRUCCION!!!!"<<std::endl;
  }

  void set_x(float v){ x_ = v;}
  void set_y(float v){ y_ = v;}
  float get_x() {return x_;}
  float get_y() {return y_;}
  void print()
  {
    std::cout<<"("<<x_<<", "<<y_<<")";
  }

private:
  float x_;
  float y_;

};

class TPila
{
private:
  Coordenada datos[MAX];
  int cima;

public:
  void init()
  {
      cima = 0;
  }

  void push(Coordenada dato)
  {
    datos[cima++] = dato;
  }

  Coordenada pop()
  {
      return datos[--cima];
  }

  void print()
  {
    for(int i=0; i< cima; i++)
      datos[i].print();
    std::cout<<std::endl;
  }

};

int main(int argc, char *argv[])
{
  //TPila pila_1, pila_2;

  //pila_1.init();
  //pila_2.init();

  Coordenada t1;// = {3.4, 12.3};
  t1.print();
  Coordenada t2(3.4, 12.3);
  t2.print();
  //t1.set_x(1);
  //t1.set_y(1);

  //Coordenada t2;// = {1.4, 12.3};
  //Coordenada t3;// = {6.4, 12.3};
  //pila_1.push(t1);
  //pila_1.push(t2);
  //pila_2.push(t3);

  //pila_1.cima = 7;
  //pila_1.print();
  //



  return 0;
}
