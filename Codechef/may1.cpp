#include<stdio.h>
using namespace std;
int main()
{

    unsigned long long int a;
    scanf("%llu",&a);

    if(a==0 || a==1){
            printf("yes\n");
        }
        else if(a%3 == 0){
            printf("yes\n");
        }
        else if((a-1)%6 == 0){
           printf("yes\n");
        }
        else{
            printf("no\n");
        }





}
