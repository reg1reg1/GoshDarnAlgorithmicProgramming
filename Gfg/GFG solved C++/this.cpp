#include<stdio.h>
#include<string.h>
#include<ctype.h>
int a[100];
void swap1(char x[])
{
    char c;
    int i;
    for(i=0;i<strlen(x);i++)
    {   c=x[i];
        x[i]=x[strlen(x)-i-1];
        x[strlen(x)-i-1]=c;
    }

}
void sort1()
{
    int i,j,temp;
    for(i=0;i<10;i++)
    {
        for(j=0;j<9-i;j++)
        {
            if(a[j]>=a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;

            }
        }
    }
}
int main()
{   int i;
    for(i=0;i<10;i++)
    {
        scanf("%d",&a[i]);
    }
     sort1();
     for(i=0;i<10;i++)
     printf("%d ",a[i]);
    return 0;
}
