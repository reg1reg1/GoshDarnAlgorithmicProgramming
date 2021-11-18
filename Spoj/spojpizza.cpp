#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<ctype.h>
#include<string.h>
using namespace std;
int main()
{
    char s[4];
    long long int t;
    int t1=0,t2=0,t3=0,count1=1;
    //printf("count1 %d\n",count1);
    scanf("%lld\n",&t);

    while(t--)
    {
       gets(s);
       if(s[2]=='2')
       t1++;
       if(s[0]=='1'&&s[2]=='4')
       t2++;
       if(s[0]=='3')
       t3++;
    }
    count1=1;

    if(t3>t2)
    {
        count1=count1+t2;
        t3=t3-t2;
        t2=0;
        count1=count1+t3;
    }

    else if(t3<=t2)
    {
        count1=count1+t3;
        t2=t2-t3;
        t3=0;

    }

    if(t2>=4)
    {
        count1=count1+t2/4;
        t2=t2-(4)*(t2/4);
    }
    if(t1>=2)
    {
        count1=count1+t1/2;
        t1=t1-(2)*(t1/2);
    }

    if(t2>2*t1)
    {
       count1=count1+t1;
       t2=t2-2*t1;
       t1=0;
    }
    else if(t2<=2*t1)
    {
        count1=count1+t2/2;
        t1=t1-(t2/2);
        t2=t2-(2)*(t2/2);
    }
    if(t1>0||t2>0)
    {
        count1++;

    }


    printf("%d\n",count1);
return 0;
}
