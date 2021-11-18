#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
using namespace std;
long long int minimum(long long int a,long long int b)
{
    if(a<=b)
        return a;
    return b;

}
long long int maximum(long long int a,long long int b)
{
    if(a<=b)
        return b;
    return a;

}
 inline void fastR(long long int *a)
{
register char c=0;
while (c<33) c=getchar_unlocked();
*a=0;
while (c>33)
{
*a=*a*10+c-'0';
c=getchar_unlocked();
}
}

 long long int arr[1000001];

int main()
{
    long long int n,k,temp,i,flag=0;

    int flag2=0;
   scanf("%lld %lld",&n,&k);
   //fastR(&n);
   //fastR(&k);
   if(k%2==0)
    flag2=1;

    for(i=0;i<=k;i++)
        {
        arr[i]=10000000;

       }

    for(i=0;i<n;i++)
    {
        //fastR(&temp);
        scanf("%lld",&temp);
        arr[temp]= minimum(minimum(i+1,n-i),arr[temp]);

    }
   // printf("The value of count2 %d\n",count2);
    /*for(i=0;i<k;i++)
    {
        printf("%lld\n",arr[i]);
    }
     */
    long long int j,u,currmin=1000009;
    j=0;
    /*for(i=0;i<=k;i++)
    {
        if(arr[i]!=10000000)
        printf("value %lld index %lld \n",i,arr[i]);
    }
*/
    u=k/2+1;//suspicious fault
    while(j<=u)
    {
        if(flag2==1&&j==k/2)
        {
            j++;
            continue;
        }

        if(arr[j]==10000000||arr[k-j]==10000000)
        {
            j++;
            continue;
        }
        else
        {
           if(currmin>maximum(arr[j],arr[k-j]))
           {
             currmin=maximum(arr[j],arr[k-j]);
             flag=1;
           }
           j++;
        }

    }
   // printf("The array min2\n");

    if(flag==0)
    printf("-1\n");
    else
    {

         printf("%lld\n",currmin);
    }



return 0;
}
