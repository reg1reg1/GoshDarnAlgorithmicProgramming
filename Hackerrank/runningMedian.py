'''
The running median problem
Problem Link: https://www.hackerrank.com/challenges/find-the-running-median/problem
Author: ys3334@nyu.edu

'''
import heapq

#median will be added and this function will be called after each addition
#a is a number which is being added 
minHeap=[]
maxHeap=[]
currentMedian=0.0

def runningMedian(a):
	n=len(a)
	i=0
	x=[]
	while i<n:
		x.append(runningMedianCore(a[i]))
		i=i+1
	return x
def runningMedianCore(a):
	global minHeap
	global maxHeap
	global currentMedian

	#Using heaps to dynamically maintain the median in O(1) time.O
	#Using a negative min heap to store the max heap


	
	sizeMin=len(minHeap)
	sizeMax=len(maxHeap)
	
	#incorportaing the new element
	
	if a>=currentMedian:#insertion will happen to minHeap
		#print("Minheap insertion")
		if sizeMin>sizeMax:
			#Have to extract from minHeap and insert to maxHeap
			elem=heapq.heappop(minHeap)
			heapq.heappush(maxHeap,elem*(-1))
		heapq.heappush(minHeap,a)
	else:#insertion will happen to maxHeap
		#print("Maxheap insertion")
		if sizeMax>sizeMin:
			#Have to extract from maxHeap and insert to minHeap
			elem=heapq.heappop(maxHeap)
			heapq.heappush(minHeap,elem*(-1))
		heapq.heappush(maxHeap,a*(-1))
	
	sizeMax=len(maxHeap)
	sizeMin=len(minHeap)
	#calculating the median

	#print("MinHeap--->",minHeap)
	#print("MaxHeap-->",maxHeap)
	if sizeMax==sizeMin and sizeMax!=0:
		currentMedian= (minHeap[0]+(-1)*maxHeap[0])/2
	elif sizeMax>sizeMin:
		currentMedian=(-1)*maxHeap[0]
	else:
		currentMedian=minHeap[0]
	
	currentMedian=round(float(currentMedian),1)
	return currentMedian


def main():
	#n = int(input().strip())
	r=[12,4,5,3,8,7]
	x=runningMedian(r)
	print(x)

if __name__ == '__main__':
	main()



