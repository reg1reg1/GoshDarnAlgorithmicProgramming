#include <iostream>
using namespace std;

long long int maxpotion(int len)
{
	long long int max=-1,num;
	for(int i=0;i<len;i++)
	{
		cin >> num;
		if(num>max)
		{
			max=num;
		}
	}
	return max;
}

int main()
{
	int t;
	cin >> t;
	while(t--)
	{
		int r,g,b,m,i,rm=-1,gm=-1,bm=-1;
		cin >> r >> g >> b >> m;
		rm=maxpotion(r);
		gm=maxpotion(g);
		bm=maxpotion(b);
		for(i=0;i<m;i++)
		{
			if(rm>=gm && rm>=bm)
			{
				rm=rm/2;
			}
			else if(gm>=rm && gm>=bm)
			{
				gm=gm/2;
			}
			else if(bm>=rm && bm>=gm)
			{
				bm=bm/2;
			}
		}
		if(rm>=gm && rm>=bm)
		{
			cout << rm << endl;
		}
		else if(gm>=rm && gm>=bm)
		{
			cout << gm << endl;
		}
		if(bm>=rm && bm>=gm)
		{
			cout << bm << endl;
		}
	}
	return 0;
}
