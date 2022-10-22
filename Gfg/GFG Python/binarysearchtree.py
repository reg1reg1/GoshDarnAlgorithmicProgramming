from tree import *



#No two elements are same in binary search tree
class BinarySearchTree(Tree):
	def __init__(self,root=None):
		super().__init__(root)

	def insert(self,data):
		if self.head is None:
			a = Node(data)
			self.head = a
		else:
			self.insertwrapped(self.head,data)

	def insertwrapped(self,obj,data):
		if obj is None:
			a = Node(data)
			obj = a
		else:
			if obj.data == data:
				print("Element already exists")
			elif obj.data < data:
				if obj.get_right() is None:
					a = Node(data)
					obj.set_right(a)
				else:
					self.insertwrapped(obj.right,data)
			elif obj.data > data:
				if obj.get_left() is None:
					a = Node(data)
					obj.set_left(a)
				else:
					self.insertwrapped(obj.left,data)

	#returns the root node of the tree after performing a delete
	def delete(self,data,obj=None):
		print(data,obj.data)
		if obj is None:
			return self.head
		#node to be deleted lies in the left subtree	
		if obj.data > data:
			obj.set_left(self.delete(data,obj.get_left()))
		#node to be delted lies in the right subtree
		if obj.data < data:
			obj.set_right(self.delete(data,obj.get_right()))
		#this is the node to be deleted
		else:
			#node has no children
			if obj.get_left() is None and obj.get_right() is None:
				#this will get captured by the calling function
				return None
			#node has 2 children
			if obj.get_left() is not None and obj.get_right() is not None:
				inorderSuccessor = self.getMinNode(obj.get_right())
				print("inorderSuccessor ",inorderSuccessor.data)
				obj.data=inorderSuccessor.data
				#python pass-by reference (objects cannot be freed)
				#inorderSuccessor=None wont work as inordersuccessor will be assigned to none
				#deleting the duplicate node, and setting the right of obj to receive this value
				obj.set_right(self.delete(inorderSuccessor.data,obj.get_right()))
				
			#only left child exists
			elif obj.get_left() is not None:
				return obj.get_left()
			elif obj.get_right() is not None:
				return obj.get_right()
		## important to return the object reference to the calling function
		return obj


	#returns the reference to node 
	def getMinNode(self,node):
		if node.get_left() is None:
			return node
		else:
			return self.getMinNode(node.get_left())

def main():
	bst = BinarySearchTree()
		
	bst.insert(10)
	bst.insert(5)
	bst.insert(14)
	bst.insert(1)
	bst.insert(7)
	bst.insert(12)
	bst.insert(25)
	bst.insert(11)
	bst.insert(13)
	bst.insert(16)
	bst.insert(30)
	bst.insert(15)
	bst.insert(17)
	print("Head of tree ",bst.getHead().data)
	bst.Inorder(bst.getHead())
	print()
	bst.delete(25,bst.getHead())
	print()
	bst.Inorder(bst.getHead())












if __name__ == '__main__':
	main()