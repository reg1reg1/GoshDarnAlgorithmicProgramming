#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
string a,b;
int subseq(int x)
{
   int c,c1;
   int i=0,j=0;
   if(x==1)
   {   c=a.length();
       c1=b.length();
       while(i<c&&j<c1)
       {
           if(a[i]==b[j])
           {
               i++;
           }
           j++;
       }
       if(i==c)
       return 1;

       return 0;
    }
    if(x==0)
    {
        c=a.length();
       c1=b.length();
       while(i<c&&j<c1)
       {
           if(a[i]==b[j])
           {
               j++;
           }
           i++;
       }
       if(j==c1)
       return 1;

       return 0;
    }
}
int main()
{
    int t;
    scanf("%d\n",&t);


    while(t--)
    {
        int l1,l2,result;
        cin>>a;
        cin>>b;
        l1=a.length();
        l2=b.length();
        if(l1>l2)
        result=subseq(0);
        else
        result=subseq(1);

        if(result==1)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;

    }
return 0;
}
