
#include <iostream>
#include<algorithm>
#include<cmath>
#include<stdlib.h>
#include<algorithm>
#include<stdio.h>

using namespace std;
long long int binary(long long int x[],long long int low,long long int high,long long int key)
{
    long long int i;
    i=(high+low)/2;
    if(x[i]==key)
    return i;
    if(x[high]==key)
        return high;
    if(x[low]==key)
     return low;
     if(x[i]<key)
     {
       return  binary(x,i,high,key);
     }
     else
     {
       return  binary(x,low,i,key);
     }
}
int main() {
	// your code goes here

	long long int n,k,p;
	scanf("%lld %lld %lld",&n,&k,&p);

	long long int arr[100005],arr2[100005],i,j;
	for( i=0;i<n;i++)
		{
			cin>>arr[i];
			arr2[i]=arr[i];
			//u obviously need the original array for A and B input
		}
		sort(arr2,arr2+n);



	for( i=1;i<=p;i++)
		{
			long long int a,b,temp;
			scanf("%lld %lld",&a,&b);
			int flag=1;
			long int long start=binary(arr2,0,n-1,arr[a-1]);
		    long long int last=binary(arr2,0,n-1,arr[b-1]);
		    //printf("Selected frogs are on cordinate\n %lld %lld",start,last);
		    if(start>last)
            {
                temp=start;
                start=last;
                last=temp;
            }
		    if(start==last)
            {
                flag=1;
            }
            for(j=start+1;j<=last;j++)
            {

                if(arr2[j]-arr2[j-1]>k)
                {
                    flag=0;
                    break;
                }

            }
                if(flag==1)
					cout<<"Yes"<<endl;
				else if (flag==0)
				    cout<<"No"<<endl;
		}



	return 0;
}
