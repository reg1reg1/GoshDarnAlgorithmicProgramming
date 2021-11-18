#include <cstdio>
#include<iostream>
using namespace std;
int main() {
	int arr[102],c1,m,t,i,max;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&c1,&m);
		max=0;
		for(i=1;i<=c1;i++)
		{
			scanf("%d",&arr[i]);
			if(arr[i]>max)
			max=arr[i];
		}
		i=1;
		while(i<=c1)
		{
			m-=max-arr[i];
			i++;
		}
		i--;
		if(m<0)
			printf("No\n");
			else
			{
				if(m%c1==0)
				printf("Yes\n");
				else
				printf("No\n");
			}
	}
	return 0;
}
