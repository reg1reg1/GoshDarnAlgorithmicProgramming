 #include<stdio.h>
long long int x[1000][2];
int y;
long long int F(long long int n)
{
int i;
long long int temp;
if(n<12)
return n;
for(i=0;i<y;i++)
{

if(x[i][0]==n)
{
    printf("entered for %d\n",x[i][0]);
    return x[i][1];
}

}
temp=F(n/2)+F(n/3)+F(n/4);
if(n>temp)
temp=n;
x[y][0]=n;
x[y][1]=temp;
y++;
return temp;
}
int main()
{
long long int n;
while(scanf("%lld",&n)>0)
{
y=0;

printf("%lu\n",F(n));
printf("%d\n",y);
}
return 0;
}
