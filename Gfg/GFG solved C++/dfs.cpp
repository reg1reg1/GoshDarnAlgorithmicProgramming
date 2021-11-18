#include<stdio.h>
#include<stdlib.h>
int a[100][100],visited[100],n;
void dfs(int i);
int main()
{
printf("Enter the no of nodes in the graph\n");
scanf("%d",&n);
int i,j;
for(i=1;i<=n;i++)
 {
  visited[i]=0;
  for(j=1;j<=n;j++)
   a[i][j]=0;
 }
printf("\rEnter adjacency matrix\n");
for(i=0;i<n;i++)
{
    for(j=0;j<n;j++)
    scanf("%d",&a[i][j]);

}
dfs(0);
return 0;
}
void dfs(int v)
{
  int i;
  visited[v]=1;
  for(i=0;i<n;i++)
  {
      if(a[v][i]==1&&visited[i]==0)
        {
            printf("\n%d---->%d",v,i);
            dfs(i);
        }
}
}
