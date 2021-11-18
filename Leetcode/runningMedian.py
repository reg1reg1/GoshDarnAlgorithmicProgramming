import heapq
class MedianFinder:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.minHeap=[]
		self.maxHeap=[]
		self.currMedian=0.0
		
	def handleInsertion(self,a):
		#Using heaps to dynamically maintain the median in O(1) time.O
		#Using a negative min heap to store the max heap
		minHeap=self.minHeap
		maxHeap=self.maxHeap
		sizeMin=len(minHeap)
		sizeMax=len(maxHeap)
		currentMedian = self.currMedian
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
		self.currMedian=currentMedian
		
	def addNum(self, num: int) -> None:
		self.handleInsertion(num)
		

	def findMedian(self) -> float:
		return self.currMedian

