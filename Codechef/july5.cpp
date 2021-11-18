#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{

	int t;
	scanf("%d",&t);
	while( t-- )
	{
	        int n;
	        scanf("%d",&n);
	       //fastR1(&n);
	        long long int score[n+1];
	        for(int i=0;i<n;i++)
                scanf("%lld",&score[i]);
	               //fastR(&score[i]);
                score[n]=0;
                int owner[n+1];
                for(int i=0;i<n;i++)
                        owner[i]=i;
                owner[n]=0;
                int q,x,y,temp;
                //fastR1(&q);
            scanf("%d",&q);
                while(q--)
                {
                        //fastR1(&temp);
                        scanf("%d",&temp);
                        //case1
                        if (temp==0)
                        {
                                scanf("%d %d",&x,&y);
                                int t1 = x, t2 = y;
                                while(x-1!=owner[x-1])
                                        x=owner[x-1]+1;
                                while(y-1!=owner[y-1])
                                        y=owner[y-1]+1;
                                owner[t1-1]=x-1;
                                owner[t2-1]=y-1;
                                if(owner[x-1]==owner[y-1])
                                {
                                        printf("Invalid query!\n");
                                        continue;
                                }
                                if (score[x-1]>score[y-1])
                                {
                                        owner[y-1]=owner[x-1];
                                }
                                else if(score[y-1]>score[x-1])
                                {
                                        owner[x-1]=owner[y-1];
                                }
                        }
                        else
                        {
                                scanf("%d",&x);
                                 while(x-1!=owner[x-1])
                                        x=owner[x-1]+1;
                                cout<<x<<endl;
                        }
                }
	}
return 0;
}
