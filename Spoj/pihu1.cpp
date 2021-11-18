#include<stdio.h>
#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{

    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,i,j,k;
        int flag;
        flag=0;
        scanf("%d",&n);
        long long int arr[n],p,temp;
        for(i=0;i<n;i++)
        scanf("%lld",&arr[i]);
        scanf("%lld",&p);
        std:sort(arr,arr+n);
        for(i=0;i<n;i++)
        {   temp=p-arr[i];
           if(flag==1)
            break;
            j=i+1,k=n-1;
            while(j<k)
            {
                if(temp<arr[j]+arr[k])
                    k--;
                else if(temp>arr[j]+arr[k])
                    j++;
                else
                {
                    flag=1;
                    break;
                }
            }
        }
        if(flag==1)
            printf("YES\n");
        else
            printf("NO\n");




    }
    return 0;
    }
