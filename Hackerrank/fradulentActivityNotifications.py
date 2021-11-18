'''

https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
Hackerrank
Author:ysingh

'''
import heapq

def fraudulentActivity(A):
	
	#Using heaps to dynamically maintain the median in O(1) time.O
	#Using a negative min heap to store the max heap
	maxheap=[]
	minHeap=[]

	sizeMin= len(minHeap)
	sizeMax = len(maxheap)
	i =0
	while i < len(A):

		if sizeMax==0:
			heapq.heappush(maxheap,(-1)*A[i])
			i=i+1
		elif sizeMin==0:
			heapq.heappush(minheap,A[i])
			i=i+1
		else:
			if sizeMax==sizeMin:
				heapq.heappush(minHeap,A[i])
			
			if sizeMax < sizeMin:
				if 
			else:

		#calculate the median
		if sizeMax==sizeMin:
			median=((-1)*maxheap[0]+minHeap[0])/2
		if sizeMax<sizeMin:
			median=minHeap[0]
		else:
			