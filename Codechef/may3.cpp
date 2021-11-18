#include<stdio.h>
#include<string.h>
#include<ctype.h>
char a[1000001];
int main()
{
    int t,fg;
    long long int c1;
    long long int c2;
    long long int prefix,i;
    scanf("%d\n",&t);
    while(t--)
    {
        c1=0,c2=0,fg=0;
        prefix=0;
        scanf("%s",a);
        //puts(a);
       if(a[0]== '>')
       {
           printf("0\n");
           continue;
       }

       for(i=0;i<strlen(a);i++)
       {
           if(a[i]== '<')
           {
               c1++;
           }
           if(a[i]=='>')
           {
               c2++;
           }
           if(c2>c1)
           {
               //printf("c1--->%lld c2----> %lld\n",c1,c2);
               printf("%lld\n",prefix);
               fg=1;
               //printf("Entered\n");
               break;
           }
           if(c1==c2)
           prefix=2*c1;
           //printf("c1--->%lld c2----> %lld\n",c1,c2);
       }
        if(fg==0)
        printf("%lld\n",prefix);





    }








return 0;
}
