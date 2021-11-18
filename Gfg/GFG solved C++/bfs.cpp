#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<queue>
#include<iostream>
using namespace std;
void bfs(int i);
int visited[100];
vector <int> V[100];
queue <int> Q;

int n;
int main()
{

    int e;
    int t1,t2,i;

cout<<"Enter the no of nodes"<<endl;
cin>>n;

cout<<"Enter the no of edges"<<endl;
cin>>e;
for(i=1;i<=n;i++)
{
    visited[i]=0;
}
while(e--)
{
  cin>>t1>>t2;
  V[t1].push_back(t2);
}
Q.push(1);
visited[1]=1;
bfs(1);

return 0;
}
void bfs(int i)
{
  if(Q.empty())
  return;
  int data;
  int x;
  //data=Q.front();
  printf("%d--->",i);
  visited[i]=1;
  Q.pop();
  vector<int>::iterator it;
  for(x=0,it=V[i].begin();it!=V[i].end();it++,x++)
  {

      if(visited[V[i][x]]!=1)
      {     //
          printf("checked visited[%d]\n",V[i][x]);
           Q.push(V[i][x]);
           visited[V[i][x]]=1;
      }

  }
  bfs(Q.front());
}
