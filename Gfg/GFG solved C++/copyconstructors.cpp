#include<iostream>
#include<stdlib.h>
using namespace std;

class Shape
{
protected:
    int length1=25;
public:
    Shape(int x)
    {
        length1=x;
        cout<<"Super constructor called"<<endl;
    }
    Shape()
    {
        cout<<"Super default constructor called"<<endl;
    }
    friend int get_length(Shape x);

};
class Square:public Shape
{
 protected:
    int length;
 public:
    Square()
    {
        cout<<"Sub default constructor called"<<endl;

    }

    Square(int g)
    {
        cout<<"Derived constructor called"<<endl;
        this->length=g;
        cout<<"length set as "<<this->length<<" whoa "<<length1<<endl;
    }

};
int get_length(Shape g)
    {
        cout<<"Get_length constructor called"<<endl;
        return g.length1;
    }
int main()
{
    //Shape j(10);
    //cout<<get_length(j);
    Square h(10);
    Shape g(25);
    //h.length=g.length1;
   // cout<<h.length1<<endl;
    //cout<<get_length(h)<<endl;
    return 0;

}
