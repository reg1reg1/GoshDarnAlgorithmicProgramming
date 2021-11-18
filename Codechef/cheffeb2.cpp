#include<stdio.h>
#include<iostream>
#include<algorithm>
int main()
{
    int n,ptr1,q,ptr,prvs=-100;
    scanf("%d",&n);
    long long int a[n],i,count;
    for(i=0;i<n;i++)
    scanf("%lld",&a[i]);
    scanf("%d",&q);
    long long int k;

    while(q--)
    {
      count =0;
      prvs=-100;
      scanf("%lld",&k);
      for(i=0;i<n;i++)
      {
          if(a[i]==k)
          { //printf("Entered\n");
           // printf("Index of searched no %d\n",i);
            ptr=i;ptr1=i;
            while(ptr!=0)
              {
                if(ptr==prvs+1)
                {
                    break;
                }

                if(a[ptr-1]>=a[i])
                    ptr--;
                else
                    break;
              }
              while(ptr1!=n-1)
              {
                  if(a[ptr1+1]>=a[i])
                    ptr1++;
                    else
                     break;
              }
              prvs=i;
           //  printf("Ptr1 %d and ptr %d\n",ptr1,ptr);
              if(ptr==ptr1)
                count=count+1;
               else if(ptr==i)
                    count=count+ptr1-i+1;
                else if(ptr1==i)
                    count=count+i-ptr+1;
              else
                count=count+ptr1-ptr+((ptr1-i)*(i-ptr))+1;
               // printf("Current count %d \n",count);
          }

      }
      printf("%lld\n",count);




    }


return 0;
}
