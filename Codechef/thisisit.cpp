#include<stdio.h>
#include<iostream>
using namespace std;
int row[105][105];
int column[105][105];
int main()
{
  int t;
  scanf("%d",&t);
  int n ,m;
  while(t--)
  {

      scanf("%d %d",&n,&m);
      int w[n][m];
      for(i=0;i<n;i++)
      {
          for(j=0;j<m;j++)
          {
              scanf("%d",&w[i][j]);
          }
      }
      int dpdiag[100][100]
      for(j=0;j<m;j++)
      {
          dpdiag[0][j]=w[0][j+1]+w[1][j]
      }

  }

return 0;
}
