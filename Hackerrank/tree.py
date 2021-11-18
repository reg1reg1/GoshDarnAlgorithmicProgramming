
def foo():
	print(socket1)
class Queue:
	def __init__(self):
		self.head=0
		self.tail=0
		self.queuelist = list()

	def Insert(self,data):
		#print("Insert called with",data)
		self.queuelist.insert(self.tail,data)
		self.tail=self.tail+1
	
	def Process(self):
		if self.head != self.tail:
			point = self.head
			self.head=self.head+1
			return self.queuelist[point]

	def getSize(self):
		return self.tail - self.head

	def getHead(self):
		return self.queuelist[self.head]

	def getTail(tail):
		return self.queuelist[self.tail]

	def printQueue(self):
		for a,lev in queuelist:
			print("Value ,", a,"level",lev)
	def empty(self):
		if self.head==self.tail:
			return True

	


queue = Queue()

class Node():
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data
		#self.visits=0
		#self.parent=None
	
	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def set_right(self,obj):
		self.right=obj

	def set_left(self,obj):
		self.left=obj




class Tree():
	global queue
	def __init__(self,root=None):
		self.head=root

	def getHead(self):
		return self.head

	def Inorder(self,object):
		if object is None:
			return

		self.Inorder(object.left)
		print(object.data,end=" >")
		self.Inorder(object.right)

	def Preorder(self,object):
		if object is None:
			return

		
		print(object.data,end=" >")
		self.Preorder(object.left)
		self.Preorder(object.right)
	

	def levelOrderTraversal(self):
		queue.Insert((self.head,0))
		curr_level=0
		#print("Queue size ",queue.getSize())
		while queue.getSize() > 0:
			#print("queuenot empty")
			pair=queue.Process()
			node=pair[0]
			lvl=pair[1]
			#print("Node ,",node,"lvl ",lvl)
			if curr_level!=lvl:
				print()
				curr_level=lvl

			print("----- ",node.data,end="------")

			if node.get_left() is not None:
				queue.Insert((node.get_left(),lvl+1))
			if node.get_right() is not None:
				queue.Insert((node.get_right(),lvl+1))
		print()



def main():
	nodea = Node('a')
	nodeb = Node('b')
	nodec = Node('c')
	noded = Node('d')
	nodee = Node('e')
	nodef = Node('f')
	nodeg = Node('g')
	nodeh = Node('h')


	nodef.set_left(nodeg)
	nodec.set_left(nodef)
	nodeb.set_left(noded)
	nodea.set_left(nodeb)
	nodea.set_right(nodec)
	nodeb.set_right(nodee)
	nodeg.set_right(nodeh)

	tree = Tree(nodea)
	tree.Inorder(tree.getHead())
	print()
	tree.levelOrderTraversal()



	





if __name__ == '__main__':
	main()

