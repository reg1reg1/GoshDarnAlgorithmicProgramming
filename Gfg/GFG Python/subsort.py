#Modified binary search to find closest lesser than or equal to
def binarysearchless(beg,end,arr,key):
	mid = int((beg+end)/2)
	if arr[mid]==key:
		return mid
	#Order of this and next command switched to provide lower index
	if arr[end]==key:
		return end

	if arr[beg]==key:
		return beg
	
	if mid == beg or mid == beg+1:
		return beg

	if key > arr[mid]:
		binarysearch(mid+1,end)

	if key < arr[mid]:
		binarysearchless(start,mid-1)

	if beg>=end:
		return beg

def binarysearchmore(beg,end,arr,key):
	mid = int((beg+end)/2)
	if arr[mid]==key:
		return mid

	if arr[beg]==key:
		return beg

	if arr[end]==key:
		return end
	
	if mid == beg or mid == beg+1:
		return mid

	if key > arr[mid]:
		binarysearch(mid+1,end)

	if key < arr[mid]:
		binarysearchless(start,mid-1)

	if beg>=end:
		return beg




def subsort():
	start=0
	end=len(a)-1
	while start < end:
		if a[start]<a[start+1]:
			start++

		if a[end-1] < a[end]:
			end--
	divstart=0
	divend=start
	div2end=len(a)-1
	div2start=end

	minval=-1
	maxval=a[divend]
	minindex=0
	maxindex=0

	for i in range(divend,div2end):
		if a[i]<min:
			minval=a[i]

		if a[i]>max:
			maxval=a[i]



