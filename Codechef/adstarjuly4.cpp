#include <iostream>
#include<math.h>

using namespace std;
long long int v[100005];
long long int p[100005];
long long int lcm(long long int a,long long int b)
{
    long long int temp,i=1;
    if(a>b)
    {
        temp=a;
        a=b;
        b=temp;
    }
    while(b%a!=0)
    {
        i++;
        b=(b%1000000007*i%1000000007)%1000000007;
    }
    return b;

}

int main()
{
    long long int t,n,k,i,c=0,ne,ans,nic;
    cin>>t;
    for(k=0;k<t;k++)
    {
        ne=0;
        ans=1;
        nic=0;
        c++;
        cin>>n;
        for(i=1;i<=n;i++)
        {
            cin>>p[i];
        }
        i=1;
        while(ne<=n)
        {
            if(v[i]==c)
            {
                if(nic!=0)
                {
                    ans=lcm(nic%1000000007,ans%1000000007)%1000000007;
                }
                i++;
                nic=0;
                if(ne==n)
                    break;
            }
            else
            {

                if(p[i]==i)
                {

                    v[i]=c;
                    nic=0;
                    i++;
                    ne++;
                }
                else
                {
                    v[i]=c;
                    i=p[i];
                    nic++;
                    ne++;

                }
            }

        }
        cout<<(ans%(1000000007))<<"\n";

    }

    return 0;
}
