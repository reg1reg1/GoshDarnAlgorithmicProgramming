#include <stdio.h>
#include <stdlib.h>
#include <math.h>

inline void fastR(long int *a)
{
register char c=0;
while (c<33) c=getchar_unlocked();
*a=0;
while (c>33)
{
*a=*a*10+c-'0';
c=getchar_unlocked();
}
}

struct order {
    int k;
    int *a;
};


int main()
{
    int n,m,i,j,t,q,r,flag,max=0;
    int count,check;
    fastR(&n);
    fastR(&m);
    int p = pow(2,m);
    struct order b[m+1];
    struct order c[m+1];
    for (i = 0; i < m; i++) {
        fastR(&b[i].k);
        b[i].a = (int *)malloc(sizeof(int)*(b[i].k + 1));
        for (j = 0; j < b[i].k; j++) {
            fastR(&b[i].a[j]);
        }
    }
    for (i = 1; i < p; i++) {
        t = 0;
        for (j = 0; j < m; j++) {
            if (i&1<<j) {
                c[t] = b[j];
                t++;
            }
        }
        count = 1;
        int ctr[20001] = {0};
        check = c[0].k;
        for (r = 0; r < c[0].k; r++) ctr[c[0].a[r]] = 1;
        for (q = 1; q < t; q++) {
                if (check + c[q].k <= n) {
                    flag = 1;
                    for (r = 0; r < c[q].k; r++) {
                        if (ctr[c[q].a[r]] == 1) {
                            flag = 0;
                            break;
                        }
                    }
                    if (flag == 1) {
                        for (r = 0; r < c[q].k; r++) ctr[c[q].a[r]] = 1;
                        count++;
                        check += c[q].k;
                    }
                }
                if (check == n) break;
        }
        if (max < count) max = count;
    }
    printf("%d\n",max);
    return 0;
}
