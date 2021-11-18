#include <iostream>
#include <stack>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{	
		int num,nmax,nmin;
		string s;
		stack <int> nummax,nummin;
		char curr_op;
		cin>>s;
		//cout<<s<<" "<<s.length()<<"\n";
		int x=(int)(s[0])-48;
		nummax.push(x);
		nummin.push(x);
		for(int i=1;i<s.length();i++)
		{
			num=(int)s[i];
			
			//if it is a number
			if(num>=48&&num<=58)
			{   
				
				if(curr_op=='+')
				{	
					nummax.top()+=num-48;
					nummin.push(num-48);
				}
				else
				{	
					nummax.push(num-48);
					nummin.top()*=num-48;
					
				}
			}
			else
			{	
				curr_op=s[i];
			}
		}
		nmax=1;
		nmin=0;
		while(!nummax.empty())
		{
			nmax*=nummax.top();
			nummax.pop();
		}
		while(!nummin.empty())
		{
			nmin+=nummin.top();
			nummin.pop();
		}
		cout<<nmax<<" "<<nmin<<"\n";
	}
	return 0;
}