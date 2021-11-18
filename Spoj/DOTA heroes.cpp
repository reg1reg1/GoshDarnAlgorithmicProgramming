#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main()
{
   int n,m,d,t,flag,i;

   scanf("%d",&t);
   while(t--)
   {
       flag=0;
       scanf("%d %d %d",&n,&m,&d);
       int dota[n];
       for(i=0;i<n;i++)
       {
           scanf("%d",&dota[i]);
       }
       for(i=0;i<n;i++)
       {
         if(dota[i]>d)
         {
             if(dota[i]%d!=0)
             flag=flag+dota[i]/d;
             else
             flag=flag+(dota[i]/d)-1;

         }
       }
       if(flag>=m)
        printf("YES\n");
       else
        printf("NO\n");

   }
}
