def hoarePartition(a,low,high):
	x= a[low]
	i=low+1
	j=high
	print(i)
	print(j)
	k=0
	while True:
		print("--------------------------------")
		print("Loop ",k)
		while i<high and a[i]< x:
			i=i+1
		while j>low and a[j] > x :
			j=j-1
		if i>=j:
			ans=j
			break
			
		temp=a[i]
		a[i]=a[j]
		a[j]=temp
		i=i+1
		j=j-1
		print("Array after partitioning ",a)
		k=k+1

	print("Pivot value after partitioning ",a[ans])
	print("Array after partitioning ",a)


def main():
	A=[13,19,9,5,12,8,7,4,11,2,6,21]
	B= [1,2,3,4,5,6,7,8,9,10,11,12]
	hoarePartition(A,0,len(A)-1)
if __name__ == '__main__':
	main()