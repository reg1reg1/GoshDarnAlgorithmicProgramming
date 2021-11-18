#include<stdio.h>
#include<stdlib.h>
int main()
{
  long long int n;

  int test;
  scanf("%d",&test);
  while(test--)
  {
   scanf("%lld",&n);
   long long int t=1;
   long long int ans=0;
   int k=0;
  while(ans<=n)
  {
      ans=(t*t+t)/2;
    //printf("%lld\n",ans);
      t++;

  }

  printf("%lld\n",t-2);
  }
return 0;
}
