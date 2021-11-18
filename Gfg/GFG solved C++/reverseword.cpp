#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
using namespace std;
class A_stack
{
private:
    int TOP;
    char arr[1000];
public:
    A_stack()
    {
        TOP=-1;
    }
    bool isempty()
    {
        if(TOP==-1)
            return true;
    }
    void push(char x)
    {
        TOP++;
        arr[TOP]=x;
    }
    char pop()
    {
        TOP=TOP-1;
        return arr[TOP+1];
    }
    int get_top()
    {
        return TOP;
    }
};


int main()
{
char s[1000];
gets(s);
printf("String is %s\n",s);
int i=0;
A_stack a;
char temp;
i=strlen(s)-1;
//c_stack j = new c_stack(100);
while(i>=0)
{
    if(s[i]!=' ')
    {
      a.push(s[i]);
      printf("Pushed--->%c\n",s[i]);
      printf("stack_TOP--->%d",a.get_top());
    }
    if(s[i]==' '&&a.isempty())
    {    printf("leading space--->",s[i]);
         printf("%c",s[i]);
         i--;



         continue;
         
    }
    else if(s[i]==' '&&!a.isempty())
    {
       printf("stack_TOP--->%d",a.get_top());
        while(!a.isempty())
       {
           temp=a.pop();
           printf("popped-->%c\n",temp);
       }
      //printf("%c",s[i]);
    }
    i--;
}
return 0;
}
