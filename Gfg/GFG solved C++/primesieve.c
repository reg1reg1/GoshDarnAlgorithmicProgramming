#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main()
{
    int m;
    scanf("%d\n",&m);

int primes[m];
for(int i=0;i<m;i++)
primes[i]=0;

for(int p=2;p*p<=m;++p)
{
 // first number <= N && p divides N
 for(int j=p;j<=m;j+=p)
 if(j != p)
 primes[j] = 1;
 }
 for(int i=0;i<m;i++)
 {
     if(primes[i]==1)
     printf("%d ",i);
 }
return 0;
}
