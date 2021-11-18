#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{

       int T;
       cin>>T;
       vector <int> ret;

       while(T>0)
       {
           vector <int> d(3);
           for(int i=0;i<3; i++)
            cin>>d[i];

           sort(d.begin(), d.end() );

           if(d[2]>=d[1]+d[0])
           {
               ret.push_back(d[2]-(d[0]+d[1]));

           }


           else
           {
               ret.push_back(0);

           }

           T--;

       }

       for(int j=0; j<ret.size(); j++)
        cout<<ret[j]<<'\n';

}
