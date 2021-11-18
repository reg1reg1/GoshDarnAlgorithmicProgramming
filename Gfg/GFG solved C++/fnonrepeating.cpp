#include <iostream>
#include <string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int n;
	cin>>n;
	char x,y;
	y='a';
	int val;
	while(n--)
	{
		cin>>x;
		y=y^x;
		cout<<y<<"\n";

	}
		
	return 0;
}	