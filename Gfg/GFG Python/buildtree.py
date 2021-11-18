'''
Given inorder and preorder tree traversals
Build the tree
Recursion
'''

from tree import *


#Inheriting from Tree class
#Python passes variable by assignment

preorder=['A','B','D','E','C','F']
inorder= ['D','B','E','A','F','C']
preptr=0

def searchArray(val):
	global preorder
	for i in range(0,len(preorder)):
		if val == preorder[i]:
			return i

def buildTreeWrapper(begin,end):
	global inorder
	global preorder
	global preptr
	print("Begin :",begin,"End :",end)
	if begin > end:
		return None
	
	a = Node(preorder[preptr])
	
	print("Element-> ",preorder[preptr])
	preptr = preptr+1

	if begin == end:
		return a


	index = inorder.index(a.data)
	print("calling left of :", a.data,"with boundaries ",begin," ",index-1)
	a.set_left(buildTreeWrapper(begin,index-1))
	print("calling  right of :",a.data,"with boundaries ",index+1," ",end)
	a.set_right(buildTreeWrapper(index+1,end))
	return a


def main():

	mytree = Tree(buildTreeWrapper(0,len(preorder)-1))
	mytree.Inorder(mytree.getHead())

if __name__ == '__main__':
	main()





	



