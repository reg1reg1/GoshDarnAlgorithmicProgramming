def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * int(n1)
	R = [0] * int(n2)

	
	for i in range(0 , n1):
		L[i] = arr[l + i]

	for j in range(0 , n2):
		R[j] = arr[m + 1 + j]

	
	i = 0	 
	j = 0	
	k = l	 

	while i < n1 and j < n2 :
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1


	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr,l,r):
	if l < r:

		# Same as (l+r)/2, but avoids overflow for
		# large l and h
		m = int((l+(r-1))/2)

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

def main():
	arr = [2, 1, 213, 53, 6, 2]
	n = len(arr)
	print ("Given array is")
	for i in range(n):
		print ("%d" %arr[i]),

	mergeSort(arr,0,n-1)
	print ("\n\nSorted array is")
	for i in range(n):
		print ("%d" %arr[i])

if __name__ == '__main__':
	main()