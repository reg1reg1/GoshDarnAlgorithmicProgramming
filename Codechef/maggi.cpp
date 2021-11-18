#include<stdio.h>
#include<string>
#include<string.h>
#include<iostream>
#include<map>
using namespace std;
char s[33];
map<string,int> m;
void func(string str,int mask)
{
    //cout<<str<<" mask="<<mask<<endl;
    int i,f=0;
    for(i=0;i<strlen(s);i++)
    {
        int k=(1<<(i+1));
        if((mask&k)==0)
        {
            //printf("@\n");
            f=1;
            func(str+s[i],mask|k);
        }
    }
    if(f==0)
    {
        if(m[str]==0)
            cout<<str<<endl;
        m[str]++;
    }
}
int main()
{
    scanf("%s",s);
    string str;
    printf("\n\n\n");
    func(str,0);
    return 0;
}
