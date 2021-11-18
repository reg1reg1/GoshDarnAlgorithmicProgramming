#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
long long int dp[300][300]={-1};
long long int solve_dp(int n , int m , int x[])
{
    if(n==0)
    return 1;

    if(n>0&&m<=0)
    return 0;

    if(n<0)
    return 0;

    if(dp[n][m]!=-1)
    return dp[n][m];

    return dp[n][m]=solve_dp(n-x[m],m,x)+solve_dp(n,m-1,x);



}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,m;
    scanf("%d %d",&n,&m);
    long long int ans;
    int coin[m];

    for(int i=0;i<m;i++)
    {
     scanf("%d ",&coin[i]);
    }
    ans=solve_dp(n,m-1,coin);

    printf("%lld",dp[n][m-1]);

    return 0;
}
