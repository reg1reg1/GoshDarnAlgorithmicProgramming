#include<stdio.h>
#include<stdlib.h>
using namespace std;
bool issafe(arr[][],int rw, int column)
{   int i,j;
    for(i=column;i>=0;i--)
    {

            if(arr[rw][i]==1)
            return false;

    }

    //diagonals
    for(i=rw,j=column;i>=0&&j<n;i--,j++)
    {
        if(arr[i][j]==1)
        return false;
    }
    for(i=rw,j=column;i<n&&j>=0;i++,j--)
    {
        if(arr[i][j]==1)
        return false;
    }
    return true;

}
bool place_Queen(int b[n][n],int col)
{
    if(col>=N)
        return true;
    //place queens column wise
    for(i=0;i<n;i++)
    {
        if(issafe(b,i,col))
            place_queen(b,col+1);

        b[i][col]=0;

    }
    return false;
}
int main()
{
    //example of backtracking
int n;
scanf("%d ",&n);

int arr[n][n];
for(i=0;i<n;i++)
{
    for(j=0;j<n;j++)
        arr[i][j]=0;
}

return 0;
}
