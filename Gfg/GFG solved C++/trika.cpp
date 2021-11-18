#include <iostream>
#include <climits>
using namespace std;
 int xpos[2]= {0,1};
 int ypos[2]= {1,0};
 int dp[100][100]={0};

 int solve(int x,int y,int h,int w)
 {
 	int min=INT_MAX;
 	//*cout<<"mmmin "<<min<<"\n";
 	//cout<<"Index "<<x<<" "<<y<<"\n"; 
 	for(int c=0;c<2;c++)
 	{
 		if((x+xpos[c]>=0 && x+xpos[c]<h)&&(y+ypos[c]>=0 && y+ypos[c]<w))
 		{    //cout<<"coordinate "<<x+xpos[c]<<" "<<y+ypos[c];
 			if(min>dp[x+xpos[c]][y+ypos[c]])
 				min=dp[x+xpos[c]][y+ypos[c]];
 		}
        
 	}
 	if(min==INT_MAX)
 	{
 		return 0;
 	}
 	//cout<<"Min returned "<<min<<"\n";
 	return min;

 }
 int  main()
 {
 	int pposx,pposy,n,m,ans;

 	cin>>n>>m;
 	cin>>pposx>>pposy;
 	int inp[n][m];
 	for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
               cin>>inp[i][j];
        }
    }
 	//dp[n-1][m-1]=inp[n-1][m-1];
 	/*for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cout<<" "<<dp[i][j];
        }
        cout<<"\n";
    }*/
 	for(int i=n-1;i>=0;i--)
 	{
 		for(int j=m-1;j>=0;j--)
 		{
            //cout<<"inp as "<<inp[i][j]<<" ";
 			dp[i][j]=inp[i][j]+solve(i,j,n,m);
 		}
 	}
    //solution
    ans=2*inp[pposx-1][pposy-1]-dp[pposx-1][pposy-1];
    if(ans>=0)
    {
        cout<<"Y "<<ans;
    }
    else
    {
        cout<<"N";
    }
    //display dp
   /* for(int i=0;i<n;i++)
 	{
 		for(int j=0;j<m;j++)
 		{
 			cout<<" "<<dp[i][j];
 		}
 		cout<<"\n";
 	}*/
 	return 0;
 }
