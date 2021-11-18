#include<stdio.h>
int a[100]={0};
int main()
{  //program to determine endianness of machine
    int c;
    int i,j;
  // program to implement simple sieve of erastothenes
  int x;

  scanf("%d",&x);
  a[0]=1;
  a[1]=1;
  for(i=2;i*i<=x;i++)
  {
      if(a[i]==1)
        continue;
        for(j=i*2;j<=x;j=j+i)
            a[j]=1;
  }
  for(i=0;i<=x;i++)
  {
      if(a[i]==0)
        printf("%d ",i);

  }
  return 0;
}

