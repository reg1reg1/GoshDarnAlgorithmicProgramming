#include<stdio.h>
#include<stdlib.h>
int main()
{
int t,temp,temp1,temp2,temp3,temp5;
int a;
unsigned long long int b;
int ans;
scanf("%d",&t);
while(t--)
{
 scanf("%d %llu",&a,&b);
 temp=a%10;
 temp1=b%4;
 temp2=(b-1)%4;
 temp3=(b+1)%4;
 temp5=b%2;

 if(b==0||temp==1)
 {
     printf("1\n");
     continue;
 }

 else if(b==1)
 {
     printf("%d\n",temp);
     continue;
 }

 else if(temp==2)
 {
     if(temp3==0)
     {
         printf("8\n");
         continue;
     }
     if(temp1==2)
     {
         printf("4\n");
         continue;
     }
     if(temp2==0)
     {
         printf("2\n");
         continue;
     }
     if(temp1==0)
     {
         printf("6\n");
         continue;
     }

 }
 else if(temp==3)
 {
    if(temp3==0)
     {
         printf("7\n");
         continue;
     }
     if(temp1==2)
     {
         printf("9\n");
         continue;
     }
     if(temp2==0)
     {
         printf("3\n");
         continue;
     }
     if(temp1==0)
     {
         printf("1\n");
         continue;
     }
 }

 else if(temp==4)
 {
       if(temp5==0)
       {
           printf("6\n");
           continue;
       }
       else
        printf("4\n");
       continue;
 }
 else if(temp==5)
 {
    printf("5\n");
    continue;
 }
 else if(temp==6)
 {
    printf("6\n");
    continue;
 }
 else if(temp==7)
 {
    if(temp3==0)
     {
         printf("3\n");
         continue;
     }
     if(temp1==2)
     {
         printf("9\n");
         continue;
     }
     if(temp2==0)
     {
         printf("7\n");
         continue;
     }
     if(temp1==0)
     {
         printf("1\n");
         continue;
     }
 }
 else if(temp==8)
 {
     if(temp3==0)
     {
         printf("2\n");
         continue;
     }
     if(temp1==2)
     {
         printf("4\n");
         continue;
     }
     if(temp2==0)
     {
         printf("8\n");
         continue;
     }
     if(temp1==0)
     {
         printf("6\n");
         continue;
     }
 }
 else if(temp==9)
 {
    if(temp5==0)
    printf("1\n");

    else
    printf("9\n");

 }

}


return 0;

}
