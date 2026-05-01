#include <iostream>

void duplica(int& v)
{
  v = v * 2;
}

int main(int argc, char* argv[])
{
  int a = 9;
  int& ra = a;

  ra = 987;

  duplica(a);

  std::cout<<a<<std::endl;

  return 0;

}
