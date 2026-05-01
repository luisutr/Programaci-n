#include <iostream>

class Base
{
public:
  Base();
  Base(int init_val);
  Base(const Base& other);
  ~Base();

  int get_value() {return a_;}

private:
    int *a_;
};

Base::Base(): a_(0)
{
  std::cout<<"Base()"<<std::endl;
}

Base::Base(int init_val): a_(init_val)
{
  std::cout<<"Base(int)"<<std::endl;
}

Base::Base(const Base& other)
{
  std::cout<<"Base(Base)"<<std::endl;
  a_ = other.a_;
}

Base::~Base()
{
  std::cerr<<"~Base()"<<std::endl;
}

void imprime(Base b)
{
  std::cout<<b.get_value()<<std::endl;
}

int main(int argc, char* argv[])
{
  Base b1(8);
  Base b2(b1); //Base b2 = b1;

  for(int i=0; i<5; i++)
  {
    Base b(i);
    imprime(b);
  }

  std::cout<<b1.get_value()<<std::endl;
  std::cout<<b2.get_value()<<std::endl;
  return 0;
}
