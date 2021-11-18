#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
inline void fastR(long int *a)
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
long int i,j,t,n,a,b,c,d,arr[3000001],temp,y,z,prv;
scanf("%ld",&t);
while(t--)
{
y=0;
z=0;
//scanf("%ld%ld%ld%ld%ld",&n,&a,&b,&c,&d);
fastR(&n);
fastR(&a);
fastR(&b);
fastR(&c);
fastR(&d);
arr[0]=d;

for(i=1;i<n;i++)
{
arr[i]=(arr[i-1]%1000000*(arr[i-1]%1000000)*a)+((b*arr[i-1])%1000000)+c;
arr[i]=arr[i]%1000000;
}
std:sort(arr,arr+n);

for(i=n-1;i>=0;i--)
{
if(i%2==0)
y+=arr[i];
else
z+=arr[i];
}
//printing abs values
if(y-z>z-y)
printf("%ld\n",y-z);
else
printf("%ld\n",z-y);
}
return 0;
}
