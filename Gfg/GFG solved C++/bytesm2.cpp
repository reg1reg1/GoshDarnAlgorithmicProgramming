#include<stdio.h>


int arr[105][105];

int dpmax(int a,int b,int c,int ind,int x_row,int x_column);
int max(int p,int q,int r);
int main()
{
int t,i,j,k,max1;
//scanint(&t);
scanf("%d",&t);
while(t--)
{

int row,column;
//scanint(&row);
//scanint(&column);
scanf("%d %d",&row,&column);
//printf("%d %d %d",t,row,column);
int maxarr[row];
for(j=0;j<column+2;j++)
{
arr[0][j]=-200;
arr[row+1][j]=-200;
}
for(i=0;i<row+2;i++)
{
arr[i][column+1]=-200;
arr[i][0]=-200;

}
for(i=1;i<row+1;i++)
{
for(j=1;j<column+1;j++)
scanf("%d ",&arr[i][j]);
}
max1=-1000;
for(j=1;j<column+2;j++)
{
maxarr[j-1]=arr[1][j]+dpmax(j,j+1,j-1,2,row,column);
if(max1<maxarr[j-1])
max1=maxarr[j-1];
}
printf("%d\n",max1);
}
return 0;
}
int dpmax(int a,int b,int c,int ind,int x_row,int x_column)
{
if(ind==x_row)
return max(arr[ind][a],arr[ind][b],arr[ind][c]);



else
return max(arr[ind][a]+dpmax(a,a+1,a-1,ind+1,x_row,x_column),arr[ind][b]+dpmax(b,b+1,b-1,ind+1,x_row,x_column),arr[ind][c]+dpmax(c,c+1,c-1,ind+1,x_row,x_column));








}
int max(int p,int q,int r)
{
if(p>=q)
{
if(p>=r)
return p;
else
return r;
}
else
{
if(q>=r)
return q;
else
return r;

}
}
