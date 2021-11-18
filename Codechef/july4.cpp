#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
long long int gcd(long long int a, long long int b)
{
	long long int r = 0;
	do
	{
		r = a % b;
		a = b;
		b = r;
	} while (b != 0);
	return a;
}

long long int lcm(long long int a, long long int b)
{
	if (a == 0 || b == 0)
	{
		return 0;
	}
	return (a * b) / gcd(a, b);
}

int main()
{
	long long int t,n,arr[100001],cnt,ans;

	scanf("%lld",&t);
	while(t--)
	{
		ans = 1;
		scanf("%lld",&n);

		for(int i = 1;i <= n;i++)
			scanf("%lld",&arr[i]);

		for(int i = 1; i <= (n-1);i++)
		{
			long long int j = i;
			cnt = 1;
			while(arr[j] != i)
			{
				j = arr[j];
				cnt++;
			}
			if(cnt%ans == 0)
				ans = cnt;

			else
				ans = lcm(ans,cnt);

			ans = ans%(1000000007);
		}
		printf("%lld\n",ans);
	}
}
