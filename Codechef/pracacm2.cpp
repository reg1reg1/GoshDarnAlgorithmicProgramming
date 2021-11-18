#include<iostream>
#include<cstdio>
#include<string>
#include<string.h>
//chef
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        char a[2100];
        scanf("%s",a);
        int i,n=strlen(a);
        for(i=n-1;i>2;i--)
        {
            if(a[i]=='F'||a[i]=='?')
            {
                if(a[i-1]=='E'||a[i-1]=='?')
                {
                    if(a[i-2]=='H'||a[i-2]=='?')
                    {
                        if(a[i-3]=='C'||a[i-3]=='?')
                        {
                            a[i]='F';
                            a[i-1]='E';
                            a[i-2]='H';
                            a[i-3]='C';
                        }
                    }
                }
            }
        }
        for(i=0;i<n;i++)
        {
            if(a[i]=='?')
                a[i]='A';
        }
        printf("%s\n",a);
    }


    return 0;
}
