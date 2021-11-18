#include<stdio.h>
#include<stdlib.h>
using namespace std;
 inline void fastR(long long int *a)
{
register char c=0;
while (c<33) c=getchar_unlocked();
*a=0;
while (c>33)
{
*a=*a*10+c-'0';
c=getchar_unlocked();
}
}
int main()
{

}
