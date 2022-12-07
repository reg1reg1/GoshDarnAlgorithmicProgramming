
#"Python is pass by reference, but the reference is passed by value (a copy is made of the reference and passed)"

class YMinHeap():
	def __init__(self,alist=None):
		if alist is None:
			self.alist=list()
			self.heapSize=0
		else:
			self.alist=alist
			self.buildHeap(self.alist)
			self.heapSize=len(self.alist)
	def getRoot(self):
		return self.alist[0]
	def getParent(self,i):
		if i==0:
			return i
		return (i-1)//2
	def getLchildPos(self,i):
		x=i*2+1
		if x>self.heapSize-1:
			return None
		return x

	def getLchild(self,i):
		x=self.getLchildPos(i)
		if x is not None:
			return self.alist[x]

	def getRchildPos(self,i):
		x=i*2+2
		if x>self.heapSize-1:
			return None
		return x

	def getRchild(self,i):
		x=self.getLchildPos(i)
		if x is not None:
			return self.alist[x]
	def insert(self,value):
		self.alist.append(value)
		curr=len(self.alist)-1
		#bubble up, swap with a parent if value is lower, repeat till you find a parent with lower value or reach root
		while curr>0:
			X=self.alist
			parent=self.getParent(curr)
			if X[curr]<X[parent]:
				X[curr],X[parent]=X[parent],X[curr]
				curr=parent
			else:
				break

	def decreaseKey(index,decrement):
		decrementVal=abs(decrement)
		self.alist[index]-=decrementVal

	def __heapify__(self,X,index):
		l=2*index+1
		r=2*index+2
		N=self.heapSize
		mmin=index
		#find the least among parent and its children, make mmin point to that index
		if l<N and X[l]<X[mmin]:
			mmin=l
		if r<N and X[r]<X[mmin]:
			mmin=r
		#if the parent is not the min node, swap parent with the mmin, mmin will now point to where the value of the parent is stored
		if index!=mmin:
			#print("Heapify called")
			X[index],X[mmin]=X[mmin],X[index]
			#print(X)
			#perform heapify (percolate down) 
			self.__heapify__(X,mmin)

	def delete(self,index):
		last=self.heapSize-1
		a[last],a[index]=a[index],a[last]
		self.alist.pop()
		self.heapSize-=1
		self.__heapify__(self.alist,index)



	# build heap
	def buildHeap(self,X):
		
		self.heapSize=len(X)
		start=self.heapSize//2-1

		for i in range(start,-1,-1):
			#print(i,end=" ")
			self.__heapify__(X,i)
		#print()
		#print(X)
	def printHeapArray(self):
		print(self.alist)

def main():
	x=[27,20,17,16,19,13,15,10,9,7,12]
	heapObj=YMinHeap(x)
	heapObj.getRoot()
	heapObj.printHeapArray()
	heapObj.insert(5)
	heapObj.printHeapArray()



if __name__ == '__main__':
	main()