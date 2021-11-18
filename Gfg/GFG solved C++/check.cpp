#include <iostream >
using namespace std;
class Point {
    int x;
public:
    Point(int x) { this->x = x; }
    Point(const Point &p) { x = p.x;}
    int getX() { return x; }
};
struct p{
int c:10;
int m:10;
int g:10;


};
void print(int x)
{
    cout<<"Int"<<endl;
}
void print(double x)
{
    cout<<"Double"<<endl;
}
int main()
{
   int a=10;
   static int x=a;
   struct p s={4,4,4};
   cout<<s.c<<" "<<s.m<<" "<<s.g<<endl;
   if(x==a)
    cout<<"ola";
   else if(x<a)
    cout<<"ola1";
    else
    cout<<"ola2";
    char j;
    long g;
    print(j);
    //print(g);
   return 0;
}
