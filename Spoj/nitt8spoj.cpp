#include<stdio.h>
int main()
{
  int t;
        scanf("%d",&t);
        while(t--)
        {
                long long int i,n,start,finish;
                scanf("%lld",&n);
                long long int a[n];
                for(i=0;i<n;i++)
                        scanf("%lld",&a[i]);
                start=0;
                finish=n-1;
                long long int temp,ans=0;
                while(start<finish)
                {

                        if(a[start]>a[finish])
                        {
                                temp=a[finish]*(finish-start);
                                finish--;
                        }
                        else
                        {
                                temp=a[start]*(finish-start);
                                start++;
                        }
                        if(temp>ans)
                        {        ans=temp;}
                }
                printf("%lld\n",ans);
        }
        return 0;
}

