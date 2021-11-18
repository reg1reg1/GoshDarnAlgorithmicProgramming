'''
#Implementation of linked list in python
Different classes have been used for creating Node
and Linked List
'''


import sys


class Node(object):
	def __init__(self,data=None,next_node=None):
		self.data=data
		self.next_node=next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node=new_next

	def set_data(self, data):
		self.data=data

class LinkedList(object):

	def __init__(self,head=None):
		self.head=head
		self.tail=head

	def setHead(self,x):
		self.head=x
	def getHead(self):
		return self.head

	def getTail(self):
		return self.tail

	def Insert(self,object):
		if self.head is None:
			self.head=object
			self.tail=object
		else:
			self.tail.set_next(object)
			self.tail=object
			object.set_next(None)

	def display(self):
		current = self.head
		while current is not None:
			print(current.data,end="->")
			current=current.get_next()
		print("--XX")

	def delete(self):
		if self.head is None:
			print("List is empty")
		else:
			self.head = self.head.get_next()
			print("List after deletion")
			self.display()
	
	def get_size_list(self,x):
		
		if x is None:
			return 0
		else:
			print("Data now ",x.get_data())
			return 1 + self.get_size_list(x.get_next())

	def get_size(self):
			return self.get_size_list(self.head)


	def ReverseList(self):
		prev = None
		current = self.head
		while current is not None:
			next = current.get_next()
			current.set_next(prev)
			prev = current
			current = next
		self.head = prev

	def ReverseRecursionUtil(self,curr,prev):
		if curr.get_next() is None:
			self.head = curr
			curr.set_next(prev)
			return

		next = curr.get_next()
		curr.set_next(prev)
		self.ReverseRecursionUtil(next,curr)

		

	def ReverseRecursion(self):
		if self.head is None:
			return None
		self.ReverseRecursionUtil(self.head,None)

'''
MergeSort(head)
head must be an instance of class Node
low and high must be primitive integer values
'''
def MergeSort(head):
	#print("Mergesort first head ",head.get_data())
	if head.get_next() is None:
		return head

	else:
		#Split the list into 2
		pfast=head
		pslow=head
		while True:
			if pfast.get_next() is None:
				curr.set_next(None)
				break

			if (pfast.get_next()).get_next() is None:
				pfast=pfast.get_next()
				curr=pslow
				pslow=pslow.get_next()
				#Splitting the list into halves
				curr.set_next(None)
				break

			pfast=(pfast.get_next()).get_next()
			curr=pslow
			pslow=pslow.get_next()
		#Now slow points to the middle of the list
		a1=MergeSort(head)
		a2=MergeSort(pslow)
		a3=Merge(a1,a2)
		return a3
'''
Recursive implementation of merging two sorted Linked List
'''
def Merge(head1,head2):
	result=Node()
	if head1 is None:
		return head2
	elif head2 is None:
		return head1
	if head1.get_data() < head2.get_data():
		result = head1
		result.set_next(Merge(head1.get_next(),head2))
	else:
		result = head2
		result.set_next(Merge(head1,head2.get_next()))
	return result


def main():
	t=int(input().strip())
	for i in range(t):
		arr=input().strip()
		arrlist=list(map(int,arr.split(" ")))
		n = len(arrlist)
		l = LinkedList()
		for i in range(n):
			n= Node(arrlist[i])
			l.Insert(n)
		#l.display()
		a4=MergeSort(l.getHead())
		l.setHead(a4)
		#l2.Insert(a4)
	l.display()


if __name__ == '__main__':
	main()






