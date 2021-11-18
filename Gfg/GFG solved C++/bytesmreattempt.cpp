#include <iostream>
#include <climits>
using namespace std;
int x[3] = {-1,-1,-1};
int y[3] = {0,1,-1};
int dp[105][105];
int iter(int i,int j,int hlimit, int wlimit)
{   
    int mmax=INT_MIN;
    for(int k=0;k<3;k++)
    {
    	if(((i-x[k]<hlimit) && (i-x[k]>=0)) && ((j-y[k]<wlimit) && (j-y[k]>=0)))
    	{    
    		if (mmax<dp[i-x[k]][j-y[k]])
    		{
    			mmax = dp[i-x[k]][j-y[k]];
    		}
    	}
    }
    return mmax;
}
int main()
{
	int t,h,w;
	cin>>t;
	while(t--)
	{   

		cin>>h>>w;
		int inp[h][w];
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				cin>>inp[i][j];
			}
		}
    //here rows are states and last row is the final state	
    //the last state or last row dp[h,0....j] will have value equal to value of element	
    for(int j=0;j<w;j++)
    {
    	dp[h-1][j]=inp[h-1][j];
    }
    for(int i=h-2;i>=0;i--)
    {
    	for(int j=0;j<w;j++)
    	{
    		dp[i][j]=inp[i][j]+iter(i,j,h,w);
    	}
    }

    int mmax=INT_MIN;
   /* //display dp
    for(int i=0;i<h;i++)
    {
    	for(int y=0;y<w;y++)
    	{
    		cout<<dp[i][y]<<" ";
    	}
    }*/
    for(int i=0;i<w;i++)
    {
    	if(mmax<dp[0][i])
    	{
    		mmax=dp[0][i];
    	}
    }
    cout<<mmax<<"\n";
	}
	return 0;
}
	