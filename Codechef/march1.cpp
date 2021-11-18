#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
    long long int n,i,temp=0,max=-1;
    scanf("%lld",&n);
    long long int w[n];
    for(i=0;i<n;i++)
    {
        scanf("%lld",&temp);
        w[i]=temp+i;
        if(max<w[i])
            max=w[i];
    }

    printf("%lld\n",max);
    }
    return 0;
    }
