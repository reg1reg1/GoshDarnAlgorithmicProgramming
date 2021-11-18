#include <iostream>
#include<algorithm>
using namespace std;

int main() {
	// your code goes here

	int n,k,p;
	cin>>n>>k>>p;

	int arr[100001],arr2[1000001];
	for(int i=0;i<n;i++)
		{
			cin>>arr[i];
			arr2[i]=arr[i];
		}
	sort(arr2,arr2+n);


	for(int i=1;i<=p;i++)
		{
			int a,b;
			cin>>a>>b;

			int start=arr[a-1];
			int last=arr[b-1];

		//	cout<<start<<" "<<last<<endl;
			int pos1=0,pos2=0;
			int diff=0;

			for(int i=0;i<n;i++)
				{

					if(arr2[i]==start)
						{
							//sum=sum+(arr2[i+1]-arr2[i]);
							pos1=i;
						}
					else if(i>pos1)
						{

							//cout<<"arr2[i]="<<arr2[i]<<" "<<"arr2[i-1]="<<arr2[i-1]<<endl;
							diff=arr2[i]-arr2[i-1];
							if(diff>3)
								{


									break;
								}

						}
					if(arr2[i]==last)
					 {  pos2=i;
					 	break;
					 }
				}
			//	cout<<"pos1="<<pos1<<" "<<"pos2="<<pos2<<endl;
				//int sum2= (pos2-pos1)*3;
				//cout<<"sum="<<sum<<" "<<"sum2="<<sum2<<endl;
				if(diff<=3)
					cout<<"Yes"<<endl;
				else if (diff>3)
				    cout<<"No"<<endl;
		}



	return 0;
}
