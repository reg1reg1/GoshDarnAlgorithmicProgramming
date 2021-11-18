# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def ino(self,node,c):
		

		if node.left is not None:
			self.ino(node.left,c)

		if c==self.k and not self.flag:
			self.flag=True
			self.ans=node.val
			return
		c=c+1

		if node.right is not None:
			self.ino(node.right,c)


	def kthSmallest(self, root: TreeNode, k: int) -> int:
		self.k=k
		self.flag=False
		c=1
		self.ino(root,c)


		return self.ans