#include<stdio.h>
#include<iostream>
#include<vector>
using namespace std;
int taken[1000]={0};
int weight[1000][1000]={0};
vector <> V;
int main()
{
int t=0,w,t1;
printf("Enter the no of edges\n");
int n,arr[2];
scanf("%d",&n);
printf("Enter edges press -1 to stop\n");
while(t!=-1)
{
printf("Enter the edge with weight\n");
scanf("%d %d %d",&t,&t1,&w);
weight[t-1][t1-1]=w;
weight[t1-1][t-1]=w;
}
return 0;
}
