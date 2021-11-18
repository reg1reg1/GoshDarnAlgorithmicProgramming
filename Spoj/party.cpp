#include<stdio.h>
#include<stdlib.h>

//an application of dynamic knapsack using bottom up computing tables
//SPOJ question: PARTY Schedule
//Author : Yuvraj Singh BE/10386/2012
int maxof(int a,int b)
{
    if(a<b)
        return b;
    else
    return a;

}
int main()
{
 int to,kp,i,j;
 while(1)
    {
      scanf("%d %d",&kp,&to);
      if(kp==0&&to==0)
      break;
      else
      {   int yo;
          yo=to;
          int v[to+1],w[to+1];
          int V[to+1][kp+1];
          for(i=1;i<=to;i++)
            {
                scanf("%d %d",&w[i],&v[i]);

            }

            //initialising for checking garbage values

                for(j=0;j<=kp;j++)
                   V[0][j]=0;


          //bottom up computation begins
         for(i=1;i<=to;i++)
         {
             for(j=0;j<=kp;j++)
             {
                 if(w[i]<=j)
                    V[i][j]=maxof(V[i-1][j],v[i]+V[i-1][j-w[i]]);
                  else
                    V[i][j]=V[i-1][j];
             }

         }
        /*
         for(i=0;i<=to;i++)
         {
             for(j=0;j<=kp;j++)
             printf("%d ",V[i][j]);
             printf("\n");
         }
                */
         int suit,k;
         suit=V[to][kp];
         for(k=kp+1;k>1;k--)
            {
            if(V[to][k-1]<suit)
                break;
            }
            suit=V[to][k];
       printf("%d %d\n",k,V[to][k]);
      }

    }


return 0;
}

