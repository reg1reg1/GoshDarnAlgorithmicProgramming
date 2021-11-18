#include<stdio.h>
long long int a[100000]={0};
long long int b[100000]={0};
long long int c[100000]={0};
int main()
{

    long int n,i;

    scanf("%ld",&n);
    long long int k,max=-1,max1=-1;
    scanf("%lld",&k);
    for(i=0;i<n;i++)
    {
        scanf("%lld",&a[i]);
        if(max<a[i])
            max=a[i];
    }
    if(k==0)
    for(i=0;i<n;i++)
    printf("%lld ",a[i]);
    else
    {
       for(i=0;i<n;i++)
       {
           b[i]=max-a[i];

       }
       for(i=0;i<n;i++)
       {
           if(max1<b[i])
            max1=b[i];
       }
        for(i=0;i<n;i++)
       {
           c[i]=max1-b[i];

       }

       if(k%2==1)
       {
           for(i=0;i<n;i++)
            printf("%lld ",b[i]);
       }
       if(k%2==0&&k!=0)
       {
           for(i=0;i<n;i++)
            printf("%lld ",c[i]);
       }
    }

 return 0;
}
