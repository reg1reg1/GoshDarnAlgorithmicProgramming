#include<iostream>
#include<stdio.h>
using namespace std;
int min(int a,int b)
{
    if(a<b)
    return a;
    return b;
}
int max(int a,int b)
{
    if(a>b)
        return a;
    return b;
}
int main()
{
 int t;
 int a,h,max1;
 scanf("%d",&t);
 while(t--)
 {
 scanf("%d %d",&h,&a);
 int m1=0,m2=0,m3=0;
 m1=2*min(h/2,a/8);
 if(h/2<a/8)
 {
     if(h%2==0)
     m1=m1-1;
    // printf("Entered1");
 }
 else if(a/8<h/2)
 {
    if(a%8==0)
    m1=m1-1;
    // printf("Entered2");
 }
 else if(a/8==h/2)
 {
     if(a%8==0||h%2==0)
     {
           m1=m1-1;
           //printf("Entered4\n");
     }

      //printf("Entered3\n");
 }

 m2=2*(h/17);
 if(h%17!=0)
 m2=m2+1;
 int temp1;
 int temp2;
 temp1=h;
 temp2=a;
 while(temp1>0&&temp2>0)
 {

 }
max1=max(m1,max(m2,m3));
//printf("%d %d %d\n",m1,m2,m3);
printf("%d\n",max1);
 }
return 0;
}
