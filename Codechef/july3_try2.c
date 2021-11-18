#include <stdio.h>
#include <stdlib.h>

typedef struct data{
	long long int a;
	long long int b;
}data;

bool compare(data x,data y)
{
   return (x.b<y.b);
}
long long int q[100008];
int main() {
	long long int n,k,p,i,x,y,l,k1;
	scanf("%lld%lld%lld",&n,&k,&p);
	struct data arr[n];

	for(i=0;i<n;i++) { scanf("%lld",&arr[i].b); arr[i].a=i;}
	qsort(arr,n,sizeof(struct data),compare);
	q[0] = 0;
	long long int w[n];
	w[arr[0].a] = 0;
	for(i=1;i<n;i++) {
		if(arr[i].b-arr[i-1].b<=k)
		q[i]=q[i-1]+1;
		else
		q[i] = q[i-1];
		w[arr[i].a] = i;
	}
	for(i=0;i<p;i++) {
		scanf("%lld%lld",&x,&y);
		l = q[w[x-1]];
		k1 = q[w[y-1]];
		x = w[x-1];
		y = w[y-1];
		if(x-y<0) {
			y = y-x;
		}
		else
		y = x-y;
		if(l-k1<0)
		k1 = k1-l;
		else
		k1 = l-k1;
		if(k1==y)
		printf("Yes\n");
		else
		printf("No\n");
	}
	return 0;
}
