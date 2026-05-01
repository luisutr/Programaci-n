#include <string>
#include <iostream>

class Vehiculo
{
public:
  Vehiculo(const std::string modelo);

  std::string getModel(){return modelo_;}
  float getVelocity(){return velocidad_;}

private:
  std::string modelo_;
  float velocidad_; // km/h
};

class Coche: public Vehiculo
{
public:
  Coche(const std::string modelo);
  void print();
private:
  int ruedas_;
};

Vehiculo::Vehiculo(const std::string modelo)
{
  modelo_ = modelo;
  velocidad_ = 0.0;
}

Coche::Coche(const std::string modelo):
  Vehiculo(modelo)
{
  ruedas_ = 4;
}

void Coche::print()
{
  std::cout<<"Coche["<<getModel()<<"\tVel = "<<getVelocity()
    <<"\truedas = "<<ruedas_<<std::endl;
}


int main(int argc, char* atgv[])
{
  Vehiculo v1("Avión de papel");
  Coche c1("Mini Cooper S");

  c1.print();

  return 0;
}
