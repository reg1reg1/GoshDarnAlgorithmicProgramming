#include <stdio.h>
#include<stdlib.h>
using namespace std;
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

bool k[1000000];
int main() {
	int t;
	scanf("%d",&t);
	while(t--)
	{
		long long int n;
		long long int a,b,c,d,s,temp;
        fastR(&n);
        fastR(&a);
        fastR(&b);
        fastR(&c);
        fastR(&d);
		for(int i=0;i<1000000;i++)
			k[i]=false;

		temp=d;
		k[d]=true;
		for(int i=1;i<n;i++)
		{
			s=(a*temp*temp + b*temp +c)%1000000;
			temp=s;
		//	cout<<"s = "<<s<<endl;
			if(k[s])
				k[s]=false;
			else
				k[s]=true;
		}

		int count=0;
		long long int sum=0;

		for(int i=0;i<1000000;i++)
		{
			if(k[i])
			{

				if(count%2==0)
					sum +=i;
				else
					sum -=i;

					count++;
			}
		}

		if(sum>=0)
			//cout<<sum<<endl;
			printf("%lld\n",sum);
		else
            printf("%lld\n",(-1)*sum);

	}
	return 0;
}
