#include <iostream>
using namespace std;

int main() {
	long t, n;
	long long cnt=0;
	string s;
	cin>>t;
	for(long i=0; i<t; i++) {
		cin>>n>>s;
		for(long j=0; j<n; j++) {
			cnt += (s[j] == '1');
		}
		if(cnt % 2 == 0) {
			cout<<(cnt/2)*(cnt+1)<<endl;
		} else {
			cout<< (cnt)*((cnt+1)/2)<<endl;
		}
		cnt=0;
	}
	return 0;
}
