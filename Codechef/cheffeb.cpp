#include<stdio.h>
#include<cstdio>
#include<algorithm>
#include<ctype.h>
#include<iostream>

using namespace std;
int main()
{
    int t,count1;
    scanf("%d",&t);
    string a,b;
    while(t--)
    {   count1=0;
        cin>>a;
        cin>>b;
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());

        int pa,pb;
        pa=0;
        pb=0;
        while(pa<=a.length()-1&&pb<=b.length()-1)
        {
            if(a[pa]==' ')
            {
             pa++;
             continue;
            }
            if(b[pb]==' ')
            {
                pb++;
                continue;
            }
             if(a[pa]==b[pb])
             {
                pa++;
                pb++;
                count1++;

            }
            else
            {
              if(a[pa]>b[pb])
              {
                  pb++;
                  continue;
              }
              else
              {
               pa++;
               continue;
              }

            }


        }
        printf("%d\n",count1);

    }



return 0;
}
