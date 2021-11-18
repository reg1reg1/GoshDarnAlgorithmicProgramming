#include <iostream>
using namespace std;
int main()
{
	int k;
	string inp;
	cin>>k>>inp;
	char zigzag[k][1005];
	//initialising
    for(int i=0;i<k;i++)
    {
    	for(int m=0;m<1005;m++)
    	{
    		zigzag[i][m]='0';
    	}
    }
	int length = inp.length();
	int num=0;
	int flag=0;
	int colno=0;
	while(num<length)
	{   
		
			    
		if(flag%2==0)
		{   //cout<<"Normal column"<<colno<<" ";
			for(int i=0;i<k;i++)
				{
					zigzag[i][colno]=inp[num];
					//cout<<"Inserted "<<inp[num]<<" ";
					num++;

					if(num>=length)
					{
						break;
					}
				}
				//cout<<"\n";
			flag++;
			colno++;
		}
		else
		{   //cout<<"Zag column "<<colno<<" ";
			for(int i=k-2;i>=1;i--)
			{
				zigzag[i][colno]=inp[num];
				//cout<<"Inserted "<<inp[num]<<" ";
				num++;
				if(num>=length)
				{
					break;
				}
			}
			//cout<<"\n";
			flag++;
			colno++;
		}
	}
	//display
	for(int i=0;i<k;i++)
	{
		for(int j=0;j<=colno;j++)
		{
			if(zigzag[i][j]!='0')
			{
				cout<<zigzag[i][j];
			}
		}
	}
	cout<<"\n";
	

	return 0;
}