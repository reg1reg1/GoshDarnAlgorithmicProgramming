from tree import *
from ysinghStack import *

def iterativePreOrder(Node):
	_myStack = Stack()
	print(Node.data,end=" >")
	_myStack.push(Node.get_right())
	_myStack.push(Node.get_left())
	curr=_myStack.top()
	while(curr is not None and _myStack.empty() is False):
		print(curr.data,end=" >")
		_myStack.pop()
		if(curr.get_right() is not None):
			_myStack.push(curr.get_right())
		if(curr.get_left() is not None):
			_myStack.push(curr.get_left())
		curr=_myStack.top() 





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

	mytree = Tree(nodea)
	mytree.Preorder(mytree.getHead())
	print()
	iterativePreOrder(mytree.getHead())


if __name__ == '__main__':
	main()



