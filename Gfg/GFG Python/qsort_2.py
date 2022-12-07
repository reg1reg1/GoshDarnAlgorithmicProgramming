#split the array along the pivot element, and return the position of the pivot
def yspartition(arr,low,high):
	i=low-1
	j=low
	pivot=arr[high]
	#print("partition ",low," ",high)
	while(j<high):
		if arr[j]<=arr[high]:
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
		j+=1
	#current position of the pivot is 1 plus the last element that was deemed swappable (being less than pivot)	
	arr[i+1],arr[high] = arr[high],arr[i+1]
	return i+1


def qsortUtil(arr,low,high):
	#print("qsortUtil ",low," ",high)
	
	if low < high:
		pi=yspartition(arr,low,high)
		#make sure pivot is not included in the partitions
		qsortUtil(arr,low,pi-1)
		qsortUtil(arr,pi+1,high)
	

def qsort(arr):
	low=0
	high = len(arr)-1
	qsortUtil(arr,low,high)
	return arr

def main():
	arr=[10,80,30,90,40,50,70]
	x=qsort(arr)
	print(x)

if __name__ == '__main__':
	main()