#include <stdio.h>
#include<malloc.h>
#include<string.h>
using namespace std;
char temp[1000001];
int main()
{
	long int l,len=0,i,j,n,count=0,maxcount=0,top;
	scanf("%ld",&n);
	for(i=0;i<n;i++)
	{
		top=-1;
		count=0;
		maxcount=0;

		scanf("%s",temp);
		l=strlen(temp);
		int stk[l];
		for(j=0;j<l;j++)
		{
			switch(temp[j])
			{
				case '<':  top++;
						   stk[top]=1;
						   break;
				case '>':  if(top!=-1)
				           {
				           		stk[top--]=0;
				           		count+=2;
				           }
				           else if(top==-1)
				           {
				           		if(count>maxcount)
				           			maxcount=count;
				           		count=0;
				           }
				           break;
				default : break;
			}
		}
		if(count>maxcount)
			maxcount=count;
		printf("%ld\n",maxcount);
	}
	return 0;
}
