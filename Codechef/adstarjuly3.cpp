#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
using namespace std;
long long int pos[100005],x[100005],ans[100005],sp[100005];
void quicksort(long long int first,long long int last){
    long long int pivot,j,temp,i;

     if(first<last){
         pivot=first;
         i=first;
         j=last;

         while(i<j){
             while(x[i]<=x[pivot]&&i<last)
                 i++;
             while(x[j]>x[pivot])
                 j--;
             if(i<j){
                 temp=x[i];
                  x[i]=x[j];
                  x[j]=temp;

                  temp=pos[i];
                  pos[i]=pos[j];
                  pos[j]=temp;
             }
         }

         temp=x[pivot];
         x[pivot]=x[j];
         x[j]=temp;

         temp=pos[pivot];
         pos[pivot]=pos[j];
         pos[j]=temp;


         quicksort(first,j-1);
         quicksort(j+1,last);
     }
}

int main()
{
    long long int n,k,p,i,a,b,c1,c2,temp,j,l;
    cin>>n>>k>>p;
    for(i=0;i<n;i++)
    {
        cin>>x[i];
        pos[i]=i+1;
    }
    quicksort(0,n-1);
    i=0;
    j=0;
    while(1)
    {
        if(abs(x[i]-x[i+1])<=k)
        {
            i++;
        }
        else
        {

        for(l=j;l<=i;l++)
        {
            ans[l]=i;
        }
        j=i+1;
        ans[j]=pos[j];
        i++;

        }
        if(i==n)
            break;
    }
    for(i=0;i<n;i++)
        {
            sp[pos[i]-1]=i;
        }

//     for(i=0;i<n;i++)
//        cout<<sp[i]<<" ";
//    cout<<"\n";
//        for(i=0;i<n;i++)
//        cout<<ans[i]<<" ";
for(i=0;i<n;i++)
{
    printf("%lld ",ans[i]);

}
printf("\n");
for(i=0;i<n;i++)
{
    printf("%lld ",sp[i]);

}

    for(i=0;i<p;i++)
    {
        cin>>a>>b;
        a--;
        b--;
        c1=sp[a];
        c2=sp[b];
        if(c1>c2)
        {
            temp=c1;
            c1=c2;
            c2=temp;
        }
        if(ans[c1]>=c2)
            cout<<"Yes\n";
        else
            cout<<"No\n";


    }

    return 0;
}
