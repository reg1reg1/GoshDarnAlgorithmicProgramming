
INT_MIN=-999999999999999




class MinHeap():
	def __init__(self,alist=None):
		if alist is None:
			self.__heap__=list()
		else:
			self.buildHeap(alist)

	def buildHeap(x):
		self.__heap__ = x
		#leaves are already valid heaps, hence we start from the first non leaf node from the right
		for i in range(len(x)/2,-1,-1):
			self.minHeapify(i)

	def isEmpty(self):
		if len(self.__heap__)==0:
			return True

	def insertVal(self,x):
		#empty case
		if(self.isEmpty()):
			self.__heap__.append(x)
			return
		self.__heap__.append(x)
		insIndex = len(self.__heap__)-1
		parent = self.getParent(insIndex)
		#recursively swap and percolate up
		while self.__heap__[parent]>self.__heap__[insIndex]:
			
			#Swap with parent of the
			temp=self.__heap__[insIndex]
			self.__heap__[insIndex]=self.__heap__[parent]
			self.__heap__[parent]=temp
			
			#make insIndex point to the correct location after swapping
			#Get parent ofc current insIndex
			insIndex=parent
			parent=self.getParent(insIndex)
		return insIndex

	def displayHeap(self):
		print(self.__heap__)

	def getMin(self):
		return self.__heap__[0]

	def displayHeapLevelWise(self):
		pass

	def getLchild(self,index):
		return index*2+1

	def getRchild(self,index):
		return (index+1)*2

	def getParent(self,index):
		return int(index/2)
	
	def extractMin(self):
		extractedMin=self.__heap__[0]
		self.__heap__[0]=self.__heap__[len(self.__heap__)-1]
		self.__heap__.pop()
		self.minHeapify(0)

	def decreaseKey(self,index,newvalue):
		self.__heap__[index]=newvalue
		#Decrease in value, so percolate up

		parent = self.getParent(index)
		while self.__heap__[parent] > self.__heap__[index]:
			#swap 
			temp = self.__heap__[index]
			self.__heap__[index] = self.__heap__[parent]
			self.__heap__[parent] = temp

			#make the current node the parent
			index = parent
			parent = self.getParent(index)
	
	def deleteKey(self,index):
		self.decreaseKey(index,INT_MIN)
		self.extractMin()

	def minHeapify(self,index):
		#assumes that the left and right subtrees are already valid heaps
		#Take the left and right child of current root
		# We are percolating downward
		#MinHeap will make a heap from this node onward (Towards bottom)
		left = self.getLchild(index)
		right = self.getRchild(index)
		minIndex = index
		if left<len(self.__heap__) and self.__heap__[left]<self.__heap__[index]:
			minIndex  = lchild
		if right<len(self.__heap__) and self.__heap__[right]<self.__heap__[minIndex]:
			minIndex = right
		if minIndex!=index:
			temp = self.__heap__[index]
			self.__heap__[index]=self.__heap__[minIndex]
			self.__heap__[minIndex]=temp
		self.minHeapify(minIndex)

def main():
	minH = MinHeap()
	minH.insertVal(3)
	minH.insertVal(2)
	minH.insertVal(1)
	minH.displayHeap()
	minH.insertVal(15)
	minH.insertVal(4)
	minH.insertVal(45)
	minH.displayHeap()

if __name__=='__main__':
	main()