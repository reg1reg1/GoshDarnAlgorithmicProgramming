

a = []

def partition(low,high):
	global a
	i=low
	j=high
	pivot = int((high+low)/2)
	#print("Partition low ",i," high",j)
	print("Pivot selected as ",a[pivot])
	#swap  pivot and low(So we do not cross pivot and involve it in swapping)
	#we have to center our elements around pivot
	if pivot!=i:
		a[pivot]=a[pivot]+a[i]
		a[i]=a[pivot]-a[i]
		a[pivot]=a[pivot]-a[i]
		pivot=i
		i=i+1
	#print("Print i and j and pivot",i," ",j," ",pivot)
	#print("Before partitioning ",a)
	while i<j:

		while a[i]<=a[pivot] and  i<j:
			i+=1
		while a[j]>a[pivot] and j>i:
			j-=1
		#print("Swapping at i,j",i," ",j)
		if(i<j):
			a[i]=a[i]+a[j]
			a[j]=a[i]-a[j]
			a[i]=a[i]-a[j]
			i+=1
			j-=1
		print(a)			
	#swap j and pivot (j marks the correct position of pivot)
	#pivot is in leftmost pos
	#left  partition can have only low values
	#once i and j cross, j will be pointing to a value which is lower than pivot
	#Hence value pointed by i and j can be swapped
	#print("After loop, need to switch j and pivot now ",a)
	if j!=pivot:
		a[pivot]=a[pivot]+a[j]
		a[j]=a[pivot]-a[j]
		a[pivot]=a[pivot]-a[j]
	
	print("After Partitioning",a[low:high])
	print("----------------------------------------------------")
	return j

def hoarePartition(low,high):
	global a
	x= a[low]
	i=low
	j=high
	while True:
		while a[i]<=a[x]:
			i=i+1
		while a[j]>=a[x]:
			j=j-1
		if i<j:
			temp=a[i]
			a[i]=a[j]
			a[j]=temp
		else:
			return j
def quicksort(low,high):
	if(low>=high):
		return
	pivot = hoarePartition(low,high)
	quicksort(low,pivot-1)
	quicksort(pivot+1,high)



def main():
	global a
	t = int(input().strip())
	for i in range(t):
		arrinp = input().strip()
		a = list(map(int,arrinp.split(" ")))
		quicksort(0,len(a)-1)
		print("SORTED",a)

if __name__ == '__main__':
	main()


		


