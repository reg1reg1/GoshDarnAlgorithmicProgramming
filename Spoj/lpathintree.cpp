#include<vector>
#include<stdio.h>
#include<iostream>
using namespace std;
int visited[10005]={0};
int fuck[10005];
vector <int> V[10010];
void dfs(int x,int g)
{
    visited[x]=1;
    int i;
    fuck[x]=g;
    for(i=0;i<V[x].size();i++)
    {
        if(visited[V[x][i]]==0)
            dfs(V[x][i],g+1);
    }
}
int main()
{
int n,t1,t2,i;
 while(scanf("%d",&n)!=EOF)
{
    for(int i=0;i<n;i++)
    {
         V[i].clear();
         visited[i]=0;
         fuck[i]=0;
    }


for(i=0;i<n-1;i++)
{
    scanf("%d %d",&t1,&t2);
    V[t1-1].push_back(t2-1);
    V[t2-1].push_back(t1-1);
}
fuck[0]=0;
dfs(0,0);
int ind=0;

for(i=0;i<n;i++)
{
    if(fuck[ind]<fuck[i])
        ind=i;

        visited[i]=0;
}
dfs(ind,0);
int max=-1;
for(i=0;i<n;i++)
{
    if(max<fuck[i])
        max=fuck[i];
}
printf("%d\n",max);
            }
return 0;
}
