#include <iostream>

class Base
{
public:
  Base();
  Base(int init_val);
  Base(const Base& other);

  int get_value() {return a_;}

private:
    int a_;
};

Base::Base()
{
  std::cout<<"Base()"<<std::endl;
  a_ = 0;
}

Base::Base(int init_val)
{
  std::cout<<"Base(int)"<<std::endl;
  a_ = init_val;
}

Base::Base(const Base& other)
{
  std::cout<<"Base(Base)"<<std::endl;
  a_ = other.a_;
}

int main(int argc, char* argv[])
{
  Base b1(8);
  Base b2(b1); //Base b2 = b1;

  std::cout<<b1.get_value()<<std::endl;
  std::cout<<b2.get_value()<<std::endl;
  return 0;
}
