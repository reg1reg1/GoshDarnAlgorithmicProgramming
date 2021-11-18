#include<stdio.h>
#include<stdlib.h>
#include<math.h>
using namespace std;
int main()
{
   int t;
   int n;

   scanf("%d",&t);
   while(t--)
   {
    scanf("%d",&n);
   long long int product;
    long long int total=0;
    int i,j;
//    sum=0;
    for(i=1;i<=n/2;i++)
    {
        j=n-i;
        //printf("j %d i %d\n",j,i);
       product=i*j;
       int temp,temp1;

       for(temp=1;temp<=sqrt(product);temp++)
       {
           if(temp*temp<product)
           {
           if(product%temp==0)
           {
               if(i==j)
               {
                 //  printf("todasdmasl");
                total=total+1+((product/temp)-temp-1)*2;
               // printf("%d ",total);
               }
               else
               {
                   total=total+2+((product/temp)-temp-1)*4;
               }

           }
           else
           {

               if(i==j)
               {
                total=total+1+((product/temp)-temp)*2;
               }
               else
               {
                   total=total+2+((product/temp)-temp)*4;
               }
           }
           }


       }
        //printf("total %d\n",total);
    }
    printf("%lld\n",total);



   }
   return 0;
}
