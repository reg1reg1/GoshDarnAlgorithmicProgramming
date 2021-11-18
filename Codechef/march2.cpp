#include<stdlib.h>
#include<stdio.h>

int main()
{
      long long int t;
     scanf("%lld",&t);
      while(t--)
      {
         long long int n,i;
         scanf("%lld",&n);

         long long int a[n];
         long long int count[3];
         count[0]=count[1]=count[2]=0;
         for(i=0;i<n;i++)
         {
              scanf("%lld",&a[i]);
              if(a[i]==0)
              count[0]++;
              else if(a[i]==1)
              count[1]++;
              else if(a[i]==2)
              count[2]++;
         }

         long long int sum = ((n)*(n-1))/2;

         long long int sum1[3];
         sum1[0]=(((count[0])*(count[0]-1))/2)+((n-count[0])*count[0]);
         sum1[1]=(((count[1])*(count[1]-1))/2)+((n-count[1]-count[0])*count[1]);
         sum1[2]=(count[2]*(count[2]-1))/2;

         long long int sum2=sum1[0]+sum1[1]+sum1[2];
         long long int result = sum-sum2;
         printf("%lld\n",result);
      }
      return 0;
}
