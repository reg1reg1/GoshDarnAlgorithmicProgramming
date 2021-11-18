#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>
long  long gcd(long long  a,long long b)
{
	if(a%b==0)
		return b;
	else
		return gcd(b,a%b);
}

long long gcdutil(long long a,long long b)
{
	if(a==b)
		return a;
	else if(a>b)
		return gcd(a,b);
	else
		return gcd(b,a);
}

int f2() { printf ("Quiz"); return 1;}
int f1() { printf ("Geeks"); return 1;}

int main()
{
    	// your code goes herechar

         int x,y,z;
         x=y=z=1;
         if(++x>y)
            printf("yes\n");

//printf("%%d",k);
return 0;

}

