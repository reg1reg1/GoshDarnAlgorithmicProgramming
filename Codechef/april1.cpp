#include <stdio.h>

int arr[2004];

void foo(){
	int i,j;
	for(i=0;i<2004;i++)
    arr[i]=0;
	arr[0]=arr[1]=1;
	for(i=2;i<=2003;i++){
		if(!arr[i]){
			for(j=i*i;j<=2003;j+=i)	arr[j]=1;
		}
	}
}

int main()
{
	foo();
	int t;
	scanf("%d",&t);
	while(t--){
		int a,b,temp;
		scanf("%d %d",&a,&b);
		int sum=a+b,i;
		i=sum+1;
		while(arr[i]==1)
        {
            i++;
        }
		//while(!arr[sum++]);
		printf("%d\n",i-(a+b));
	}
	return 0;
}
