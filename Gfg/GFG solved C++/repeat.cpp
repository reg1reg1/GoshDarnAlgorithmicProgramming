#include <iostream>
using namespace std;

class A
{
private:
    int x;
public:
    A(int _x)  {  x = _x; }
    A() {}
    int get()  { return x; }
};

class B:public A
{
     static A a;
public:
    static int get()
   {  return a.get();
   }
};

int main(void)
{
    B b;
    cout << b.get();
    return 0;
}
