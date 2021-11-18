#include <iostream>
#include <string>
#include <limits>
#include <string.h>
#include <stdio.h>
using namespace std;
int mmin(int x, int y)
{
  if(x>y)
    return y;
  return x;
}
int main()
{
  int t,n,m;
  char x[5000];
  char y[5000];
  cin>>t;
  while(t--)
  {
    /*getline(cin,x);
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n'); 
    getline(cin,y);
    cin.ignore( numeric_limits<std::streamsize>::max(), '\n') ;*/
    scanf("%s",x);
    scanf("%s",y);
    m = strlen(x);
    n = strlen(y);
    int dp[m+1][n+1];
    int i,j;
    for (i=0; i <= m;i++)
    {
      for(j=0;j <= n;j++)
      {
          if(i==0)
            dp[i][j]=j;
          else if(j==0)
            dp[i][j]=i;
          else if(x[i-1]==y[j-1])
          {
            dp[i][j]=dp[i-1][j-1];
          }
          else
          {
            dp[i][j] = 1 + mmin(dp[i-1][j],mmin(dp[i-1][j-1],dp[i][j-1]));
          }
      }
    }
    cout<<dp[m][n]<<"\n";
  }
  return 0;
}