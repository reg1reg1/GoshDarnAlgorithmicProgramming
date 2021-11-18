#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int ffind(int n)
{
    int ans=0;
    if(n==1)
    return 1;
    if(n==2)
        return 2;
    else
     return ffind(n-1)+ffind(n-2);

}
int main() {
    int ans=0,n=0;
    scanf("%d",&n);
    ans=ffind(n);
    printf("%d",ans);
    return 0;
}
