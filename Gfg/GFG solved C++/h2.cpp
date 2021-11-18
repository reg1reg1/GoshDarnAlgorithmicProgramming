#include<stdio.h>
#include<stdlib.h>
int main()
{   int t;
    scanf("%d",&t);
    int ans;
    int x,y;
    int n,m;
    while(t--)
    {   x=1;
        scanf("%d %d",&n,&m);
        if(n<m)
        {
            while(x<=n&&(x*x)<(n*m))
            {
                x++;
                x<=(n*n);
            }

        }
        else if(m<n)
        {
            x=n/m;
            y=(n-x*m)*m;
            ans=x+y;

        }
        else
        {
            printf("1\n");
            continue;
        }
        printf("%d\n",ans);
    }


return 0;
}
