#include <iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int main()
{
	int t, i, j, start, high, mid, coun;
	string a, b;
	cin>>t;
	while(t--)
	{
		cin>>a;
		cin>>b;
		start=0;
		high=b.size()/a.size()+1;
		while(high-start>1)
		{
			mid=(start+high)/2;
			//cout<<mid;
			j=0;
			for(i=0; i<a.size(); i++)
			{
				for(coun=0; j<b.size() && coun<mid; j++)
					if(a[i]==b[j])
						coun++;
				if(coun==mid)
					continue;
				else
					break;
			}
			if(i!=a.size())
				high=mid;
			else
				start=mid;
		}
		cout<<start<<endl;
	}
	return 0;
}
