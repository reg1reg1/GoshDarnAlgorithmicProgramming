#include <stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

int main()
{

	long long int m,n,p=0,res,d,i,arr[100009];
	char temp;
	cin>>n>>m;
	//printf("%lld",m);
	for(i=0;i<n;i++)
    {
        cin>>arr[i];
    }

	while(m--)
	{

		cin>>temp>>d;
		//printf("M---->%lld\n",m);
		if(temp=='R')
		{
			res=(d%n)+p-1;

			//printf("p here is ------>%d",p);
			printf("%lld\n",arr[(p+d-1)%n]);
		}
		else if(temp=='C')
		p=(p+d)%n;
			//printf("p here is ------>%d",p);
		else if(temp=='A')
		{
		    p=(p-d+n)%n;
		}
		/*for(i=0;i<n;i++)
        {
            printf("%lld ",arr[(i+p)%n]);
        }
        printf("\n");
        */
			//printf("p here is ------>%d",p);

	}

	return 0;
}
