#include<cstdio>
#include<string>
#include<string.h>
#define n (1000000000+7)
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        long long int l=1;
        char a[100000];
        scanf("%s",a);
        long long int i,j;
        j=strlen(a);
        for(i=0;i<j;i++)
        {
            if(a[i]=='l')
            {
                if(l%2!=0)
                {
                    l=(l*2)%n;
                }
                else
                {
                    l=((l*2)%n-1+n)%n;

                }
            }
            else
            {
                if(l%2!=0)
                {
                    l=((l*2)%n+2)%n;
                }
                else
                {
                    l=((l*2)%n+1)%n;
                }
            }

        }
        printf("%lld\n",l);
    }
    return 0;
}
