#include <stdio.h>
using namespace std;

int main() {
long  int start;
long  int end;
long int t;
long int count;
scanf("%ld",&t);
while(t--)
    {
	count=0;
	scanf("%ld %ld",&start,&end);

while(start!=end){
				if(start>end)
					start = start/2;
				else
					end = end/2;
				count++;
			}
			printf("%ld\n",count);

}
return 0;
}
