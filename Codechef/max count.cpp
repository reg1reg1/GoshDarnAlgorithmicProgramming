#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main()
{
 int i,t,a[105],count=-1,n,index,range=-1;
 int hash[10005];

 scanf("%d",&t);
 while(t--)
 {
     scanf("%d",&n);
     count=0;
     index=0;
     for(i=0;i<=range;i++)
 {
     hash[i]=0;
 }

     for(i=0;i<n;i++)
     {
     scanf("%d",&a[i]);
     if(range<a[i])
        range=a[i];
     hash[a[i]]++;

     }

     for(i=range+1;i>0;i--)
     {

         if(count<=hash[i])
         {
             count=hash[i];
             //printf("Entered");
             index=i;
         }

     }
     printf("%d %d\n",index,count);

 }
 return 0;
}
