'''
Tell if a given binary tree is BST or not.
Uses O(n) space to store the inorder traversal of the tree and sees if that is sorted.
Temp array can actually be avoided.Store just the previously visited node and see if that is less than
the current node.
'''
from tree import *
arr=[]
def inorderAppend(root):
	global arr
	if root is None:
		return
	if root.left is not None:
		inorderAppend(root.left)
	arr.append(root.data)
	if root.right is not None:
		inorderAppend(root.right)

	

def check_binary_search_tree_(root):
	global arr
	arr=[]
	inorderAppend(arr)
	for i in range(1,arr):
		if a[i]>=a[i+1]:
			return False
	return True

def main():

if __name__ == '__main__':
	main()