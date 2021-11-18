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

	def delete(self,obj,data):
		if obj is None:
			print("Element not found")
		else:
			if data < obj.data:
				obj.set_left(self.delete(obj.get_left()))
			elif data > obj.data:
				obj.set_right(self.delete(obj.get_right()))



			


	def getMinNode(self,node):
		if node.get_left() is None:
			return node
		else:
			return self.getMinNode(node.get_left())

def main():
	bst = BinarySearchTree()
		
	bst.insert(20)
	bst.insert(10)
	bst.insert(30)
	bst.insert(25)
	bst.insert(50)
	bst.insert(40)
	bst.insert(15)
	print("Head of tree ",bst.getHead().get_left().data)
	bst.Inorder(bst.getHead())
	print()
	bst.delete(bst.getHead(),25)
	print()
	bst.Inorder(bst.getHead())












if __name__ == '__main__':
	main()