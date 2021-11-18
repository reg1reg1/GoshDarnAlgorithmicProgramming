#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
	//code
	int t;
	cin>>t;
	string arr;
	while(t--)
	{
	    cin>>arr;
	    int index=0;
	    bool exists = false;
	   // cout<<arr.length();
	    for(int i=arr.length()-1;i>=0;i--)
	    {
	        if(arr[i-1]<arr[i])
	        {   
	        	index=i;
	            exists=true;
	            break;
	        }
	    }
	    cout<<"index "<<index<<"\n";
	    if(exists)
	    {   int mmin=INT_MAX;
	    	int temp,k;
	        for(int i=index;i<arr.length();i++)
	        {
	            if (arr[i]<mmin && arr[index-1]<mmin)
	            {
	            	mmin = arr[i];
	            	k=i;
	            }

	        }
	        cout<<k;
	        temp = arr[index-1];
	        arr[index-1]=arr[k];
	        arr[k]=temp;
	        sort(arr.begin()+k,arr.end());
	        cout<<arr;

	    }
	    else
	    {
	        cout<<"-1";
	    }
	}
	
	return 0;
}