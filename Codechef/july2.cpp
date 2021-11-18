#include<stdio.h>

long long foo( long long int, long long int, long long int, long long int, char);

int main(){
	long long int t,x,y;

	scanf("%lld",&t);
	while(t--){

		scanf("%lld%lld",&x,&y);

		printf("%lld\n",foo(x,y,0,0,'0'));
	}
	return 0;
}
long long foo(long long int rx,long long int ry,long long int x,long long int y,char mod){

	if(x==rx&&y==ry)
		return 0;

	//printf("%lld   %lld   \n",x,y);

	if(mod=='0'){
		if(ry-y>0)
			return 1+foo(rx,ry,x,y+1,'1');
		else
			return 1+foo(rx,ry,x,y-1,'1');
	}
	else{
		if(rx-x>0)
			return 1+foo(rx,ry,x+1,y,'0');
		else
			return 1+foo(rx,ry,x-1,y,'0');
	}


}
