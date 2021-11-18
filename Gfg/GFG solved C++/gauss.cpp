#include<stdio.h>

int main()
{
int i,j,k,n;
float a[10][10],c[10],x[10];
printf("****** welcome 2 gauss elimination method *******\n");
printf("\nenter the number of elements: ");
scanf("%d",&n);
printf("Enter constants: ");
for(i=0;i<n;i++)
scanf("%f",&c[i]);
printf("\nenter the matrix: ");
for(i=0;i<n;i++){
for(j=0;j<n;j++)
scanf("%f",&a[i][j]);
}
for(k=0;k<n-1;i++){
for(i=k+1;i<n;i++)
{
for(j=k+1;j<n;j++)
{

a[i][j]=a[i][j]-(a[i][k]/a[k][k])*a[k][j];
c[i]=c[i]-(a[i][k]/a[k][k])*c[k];
}
}
      x[n-1]=c[n-1]/a[n-1][n-1];
      printf("The solution is: \n");
      printf("x[%d]=%f\n",n-1,x[n-1]);
      for(k=0;k<n-1;k++)
      {
        i=n-k-2;
for(j=i+1;j<n;j++)
c[i]=c[i]-(a[i][j]*x[j]);
x[i]=c[i]/a[i][i];
printf("x[%d]=%f\n",i,x[i]);
      }

      }
      return 0;
}
