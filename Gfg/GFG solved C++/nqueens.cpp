#include<stdio.h>
#include<stdlib.h>
using namespace std;
bool issafe(int *arr,int rw, int column, int n)
{   int i,j;
    for(i=column;i>=0;i--)
    {

            if(*(arr+i*n+j)==1)
            return false;

    }

    //diagonals
    for(i=rw,j=column;i>=0&&j>=0;i--,j--)
    {
        if(*(arr+i*n+j)==1)
        return false;
    }
    for(i=rw,j=column;i<n&&j>=0;i++,j--)
    {
        if(*(arr+i*n+j)==1)
        return false;
    }
    printf("Exited as true\n");
    return true;

}
bool place_Queen(int *b,int col,int n)
{   int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
            printf("%d ",*(b+i*n+col));
    }
    printf("Current column and n %d %d\n",col,n);
    if(col>=n)
    {
        return true;
    }

    //place queens column wise
    for(i=0;i<n;i++)
    {


        if(issafe(b,i,col,n)==true)
        {
            *(b+i*n+col)=1;
            printf("Queen placed at %d,%d\n",i,col);
            if(place_Queen(b,col+1,n)==true)
                return true;

           *(b+i*n+col)=0;
        }


        //b[i][col]=0;

    }
    return false;
}
int main()
{
    //example of backtracking
int n;
scanf("%d",&n);
int i,j;
int arr[n][n];
for(i=0;i<n;i++)
{
    for(j=0;j<n;j++)
        arr[i][j]=0;
}
int *p;
//printf("Number ->%d ",*(p+3*n+0));
place_Queen(p,0,4);
printf("Successful termination\n");
for(i=0;i<n;i++)
{
    for(j=0;j<n;j++)
    {
        if(arr[i][j]==1)
            printf("Q\t");

        else
            printf("*\t");
    }
    printf("\n");
}
return 0;
}
