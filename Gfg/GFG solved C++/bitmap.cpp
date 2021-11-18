#include<stdio.h>
#include<iostream>
#include<vector>
#include<queue>
#include<malloc.h>
#define max 3000
using namespace std;
int minimum(int a,int b)
{
    if(a<b)
        return a;
    return b;
}
/*
inline void fastR(int *a)
{
register char c=0;
while (c<33) c=getchar_unlocked();
*a=0;
while (c>33)
{
*a=*a*10+c-'0';
c=getchar_unlocked();
}
}
*/

using namespace std;
struct node
{
    int i;
    int j;
    int val;

};

node *newnode(int i,int j,int v)
{
    struct node *nn;
    nn=(struct node*)malloc(sizeof(struct node));
    nn->i=i;
    nn->j=j;
    nn->val=v;
    return nn;
}
void bfs()
{
     queue<struct node*> q;
    struct node *t,*nn;
    int x,y,i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i][j]==1)
            {
                nn=newnode(i,j,0);
                q.push(nn);
                ans[i][j]=0;
            }
        }
    }
    while(!q.empty())
    {
        t=q.front();
        q.pop();
        vis[t->i][t->j]=1;
        if(ans[t->i][t->j]==-1 || ans[t->i][t->j]==0)
        {
        ans[t->i][t->j]=t->val;

            x=t->i;
            y=t->j;
            x=x-1;
            if(x>=0 && a[x][y]==0 && vis[x][y]==0)
            {
                nn=newnode(x,y,(t->val)+1);
                q.push(nn);
            }
            x=x+1;
            y=y-1;
             if(y>=0 && a[x][y]==0 && vis[x][y]==0)
            {
                nn=newnode(x,y,(t->val)+1);
                q.push(nn);
            }
            y=y+1;
            x=x+1;
             if(x<n && a[x][y]==0 && vis[x][y]==0)
            {
                nn=newnode(x,y,(t->val)+1);
                q.push(nn);
            }
            x=x-1;
            y=y+1;
             if(y<m && a[x][y]==0 && vis[x][y]==0)
            {
                nn=newnode(x,y,(t->val)+1);
                q.push(nn);
            }
            y=y-1;
        }

        }
}
int main()
{
    int t,k,i,j;
    cin>>t;
    for(k=0;k<t;k++)
    {
    cin>>n>>m;
    for(i=0;i<n;i++)
    {
        cin>>ch;
        for(j=0;j<m;j++)
        {
            a[i][j]=ch[j]-'0';
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            vis[i][j]=0;ans[i][j]=-1;
        }
    }

    bfs();
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            cout<<ans[i][j]<<" ";
        }
        cout<<"\n";
    }
    }

    return 0;
}




  {
      ans[i][j]=0;
  }
  int index,res;
  pair <int,int> temp;
  visited[i][j]=1;
  Q.pop();

  for(index=0;index<4;index++)
  {
      //printf("%d %d\n",i+x[index],j+y[index]);
      if(i+x[index]>=0&&i+x[index]<n&&j+y[index]>=0&&j+y[index]<m&&visited[i+x[index]][j+y[index]]==0)
      {
          temp.first=i+x[index];
        //printf("gadbad\n");
          cout<<"Pushed"<<i+x[index]<<" "<<j+y[index]<<endl;
          temp.second=j+y[index];
          visited[i+x[index]][j+y[index]]=1;
          Q.push(temp);

      }

  }

//printf("a[%d][%d]=1+ bfs(%d,%d)\n",i,j,(Q.front()).first,(Q.front()).second);
//visited[i][j]=1;
 cout<<"Node "<<(Q.front()).first<<" "<<(Q.front()).second<<" "<<"with value"<<ans[i][j]<<endl;
 return bfs((Q.front()).first,(Q.front()).second,ans[i][j]);


}
int main()
{
//fastR(&t);
int t,q,r,i1,i2;
scanf("%d",&t);
 pair <int,int> temp;
while(t--)
{
    //fastR(&n);
    //initialise visited

    scanf("%d",&n);
    scanf("%d",&m);
    for(q=0;q<n;q++)
    {
        for(r=0;r<m;r++)
            {
            visited[q][r]=0;

            ans[q][r]=-1;

            }
    }
    //int flag=0;
    for(q=0;q<n;q++)
    {
        for(r=0;r<m;r++)
        {
           //fastR(&a[i][j]);
           scanf("%d",&a[q][r]);
           if(a[q][r]==1)
           {
                 ans[q][r]=0;
                 temp.first=q;
                 temp.second=r;
                 Q.push(temp);
                 visited[q][r]=1;
                // cout<<"Pushed"<<q<<r<<endl;
           }

        }
    }

   bfs((Q.front()).first,(Q.front()).second,0);
    for(q=0;q<n;q++)
    {
        for(r=0;r<m;r++)
        {
            printf("%d ",ans[q][r]);
        }
          printf("\n");
    }




}
return 0;
}
