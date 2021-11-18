#include <stdio.h>
#define MOD (1000000000+7)
int main(void) {

	int t,node=1,l,i;
	long long n;
	char str[100000],c;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",str);
		n=node=1,l=1,i=0;
		while(str[i]!='\0')
		{
			c=str[i++];
			if(l==1)
			{
				if(c=='l')
					n=node*2;
				else
					n=node*4;
			}
			else if(l%2==0)
			{
				if(c=='l')
					n=((node*2)%MOD-1+MOD)%MOD;
				else
					n=(node*2+1)%MOD;
			}
			else
			{
				if(c=='l')
					n=(node*2)%MOD;
				else
					n=(node*2+2)%MOD;
			}
			l++;
			node=n;

		}

		printf("%lld\n",n);
	}
	return 0;
}
