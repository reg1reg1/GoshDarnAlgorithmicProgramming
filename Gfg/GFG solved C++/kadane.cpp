#include <iostream>
#include <climits>
using namespace std;
long long int mmax(long long int x, long long int y)
{
	if(x>y)
	{
		return x;
	}
	return y;
}
int main()
{	
	int t;
	cin>>t;
	while(t--)
	{
		int n;
	long long int* a=NULL; 
	bool flag = false;
	cin>>n;
	a = new long long int[n];
	long long int ncgsum = 0;
	long long int ncgmin = LLONG_MIN;
	for(int i=0;i<n;i++)
	{	

		cin>>a[i];
	}
	for (int i = 0; i < n; i++)
	{
		if(a[i]>=0)
		{
			flag=true;
			ncgsum+=a[i];
		}
		else
		{
			if(ncgmin<a[i])
			{
				ncgmin=a[i];
			}
		}

	}

	long long int sum=0,maxsum=LLONG_MIN;
	for(int i=0;i<n;i++)
	{
		sum = sum+a[i];
		maxsum = mmax(maxsum,mmax(sum,a[i]));
		if(maxsum==a[i])
		{
			sum=a[i];
		}
	}
	
	if(flag)
	{
		cout<<maxsum<<" "<<ncgsum<<"\n";
	}
	else
	{

		cout<<maxsum<<" "<<ncgmin<<"\n";
	}	
	
	}
	
	return 0;
}
