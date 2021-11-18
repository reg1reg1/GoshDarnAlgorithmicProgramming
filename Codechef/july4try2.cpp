#include <stdio.h>
#include<math.h>
#include<iostream>
using namespace std;
    unsigned long long int gcd(unsigned long long int a, unsigned long long int b){
    if(a==0)return b;
    if(b==0)return a;
    return gcd(b%1000000007,(a%b)%1000000007);
    }
    unsigned long long int lcm(unsigned long long int a, unsigned long long int b){
    return ((a%1000000007)*(b%1000000007)/gcd(a,b))%1000000007;
    }
    int main()
    {
    unsigned long long int r,i,j,k,n,t,arr[100005],ans,loops[100005],count,start,len,gcount;
    r=scanf("%llu",&t);
    while(t--){
    r=scanf("%llu",&n);
    for(i=1;i<=n;i++){
    r=scanf("%llu",&arr[i]);
    }
    count = 0;
    for(i=1;i<=n;i++){
    start = i;
    len = 0;
    if(arr[i] == 0){
    continue;
    }
    j = arr[i];
    len++;
    arr[i] = 0;
    while(arr[j]!=0){
    k = j;
    j = arr[j];
    arr[k] = 0;
    len++;
    }
    loops[count] = len;
    count++;
    }
    gcount=0;
    for(i=0;i<count;i++){
    // printf("%llu \n",loops[i]);
    gcount = gcd(gcount,loops[i]);
    }
    ans = 1;
    for(i=0;i<count;i++){
    ans = ((ans) % 1000000007)*((loops[i] % 1000000007)/(gcount) % 1000000007);
    if(ans > 1000000007){
    	ans = ans % 1000000007;
    }
    }
    ans = ((ans % 1000000007)*(gcount % 1000000007)) % 1000000007;
    if(ans > 1000000007){
    	ans = ans % 1000000007;
    }
    printf("%llu\n",ans);
    }

    return 0;
    }
