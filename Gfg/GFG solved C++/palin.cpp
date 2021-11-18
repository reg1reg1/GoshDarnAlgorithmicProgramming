#include<stdio.h>
char a[1000000],b[1000000];
//int checkpal(long long int n)
//{
//    long long int i,f=0,l=n-1;
//    int flag=0;
//    while(f<l)
//    {
//        if(b[f]!=b[l])
//        {
//            flag=1;
//            break;
//        }
//        else
//        {
//            f++; l--;
//        }
//    }
//
//    if(flag==0)
//        return 1;
//    else
//        return 0;
//
//}
// int checkgr(long long int n)
// {
//     int f=-1;
//     long long int i;
//     for(i=0;i<n;i++)
//     {
//         if(a[i]>b[i])
//         {
//            f=1;
//         break;
//         }
//         else if(a[i]<b[i])
//         {
//             f=0; break;
//         }
//     }
//     if(f==0)
//        return 1;
//     else
//        return 0;
//
// }

int main()
{
    long long int n,t,k=1,i,f,l,z=0;
    int done=0;
    scanf("%lld",&t);
    while(k<=t)
    {
        scanf("%s",a);
        n=strlen(a);
        for(i=0;i<n;i++)
            b[i]=a[i];
        if(n==1)
        {
            if(b[0]!='9')
            {
                b[0]=b[0]+1;
            }
            else
            {
                b[0]='1'; b[1]='1';
                n=2;
            }
        }
        else
        {
            z=0;
            for(i=0;i<n;i++)
            {
                if(b[i]=='9')
                    z++;
            }
            if(z==n)
            {
                b[0]='1';
                for(i=1;i<=n;i++)
                    b[i]='0';
            b[n]='1';
        n++;

            }
            else
            {
                f=0; l=n-1;
                if(n%2!=0)
                {    int mid=(n-1)/2;
                    while(f<=l)
                    {

                        a[right]=a[left];
                      if(left==right)
                       {
                          if(strcmp(original,a)>=0)
                             {
                                 if(a[mid]!='9')
                                  a[mid]++;
                                   else
                                   {
                                    a[mid]='0';
                                    for(p1=mid-1,p2=mid+1;p1>=0,p2<=length;p2++,p1--)
                                    {
                                      if(a[p1]!='9')
                                         {
                                            a[p1]++;
                                            a[p2]=a[p1];
                                             break;
                                            }
                                           else
                                           {
                                             a[p1]='0';
                                             a[p2]=a[p1];
                                            }
                                      }
                                    }
                                   }
                                 }
                       left++;right--;
                      }
                }
                else
                {
                    while(f<=l+1)
                    {
                        //if(checkgr(n)==1 && checkpal(n)==1)
                        //{
                          //  done=1; break;
                        //}
                        if(b[f]==b[l])
                        {
                            f++; l--; continue;
                        }
                        else
                        {
                            b[l]=b[f];
                            //if(checkgr(n)==1 && checkpal(n)==1)
                            //{
                              //  done=1; break;
                            //}

                                f++; l--;

                        }
                    }
                   // f--; l++;
                    if(strcmp(b,a)<=0)
                    {
                        if(b[f]=='9' && b[l]=='9')
                        {
                            b[f]='0'; b[l]='0';
                            f--; l++;
                            while(b[f]=='9' && b[l]=='9' && f>=0 && l<n)
                            {
                                b[f]='0'; b[l]='0'; f--; l++;
                            }
                            b[f]++;
                            b[l]=b[f];
                          //  if(checkpal(n)==1 && checkgr(n)==1)
                            //    done=1;
                    }
                    else
                    {
                        b[f]++;
                        b[l]=b[f];
                    }
                }


            }

        }
        }
        for(i=0;i<n;i++)
        {
            printf("%c",b[i]);
        }
        printf("\n");
        done=0;
        n=0;




        k++;
    }
    return 0;


}



















