#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int main(){
	 int n,m,count[10],i,j,k,ans[100001];
	scanf("%d %d",&n,&m);
	char s[1000005];
	//string s="";
	scanf("%s",s);
	for(i=0;i<10;i++)count[i]=0;
	for(i=0;i<n;i++){
		ans[i]=0;
		count[s[i]-'0']++;
		for(j=0;j<10;j++){
			if(j>(s[i]-'0'))
				ans[i]+=(count[j]*(j-(s[i]-'0')));
			else
				ans[i]-=(count[j]*(j-(s[i]-'0')));
		}
	}
	for(i=0;i<m;i++){
		scanf("%d",&j);
		printf("%d\n",ans[j-1]);
	}
	return 0;
}
