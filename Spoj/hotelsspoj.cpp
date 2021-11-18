#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<stdlib.h>
using namespace std;

int main()
{
   unsigned long long int m,n,max=-1,sum,i,j,total=0,buy;
    scanf("%llu %llu",&n,&m);
    long long int a[n];
    for(i=0;i<n;i++)
    {
        scanf("%llu",&a[i]);
        total+=a[i];
    }
    if(total<=m)
    {
        printf("%llu",total);
    }
    else
   {
        i=0;
        j=0;
        max=a[i];
        buy=a[i];
        while(j<n&&max<m)
        {
            if(buy==m)
            {
                max=buy;
                break;
            }
            else if(buy>m)
            {
                buy-=a[i];
                i++;
                while(j<i)
                {
                    j++;
                }
            }
            else if(buy<m)
            {
            j++;
            buy+=a[j];


            }
             if(max<buy&&buy<m)
                {
                  max=buy;
                }
        }

    }
    printf("%llu\n",max);

    return 0;
    }
