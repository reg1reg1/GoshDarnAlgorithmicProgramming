# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def buildTreePost(self,begin,end):
		#recusion termination condition
		if begin > end:
			return None
		#traverse rightward in the post order array	(1st element we will encounter will be root, then root of right subtree and so on)
		a = self.P[self.buildIndex]
		self.buildIndex-=1
		nodeObj = TreeNode()
		nodeObj.val=a
		
		if begin==end:
			return nodeObj


		division = self.I.index(a)
		#the order of these 2 statements are imp. We will find the root to right subtree before the left one so we can't change the order (buildindex is decrementing outside the recursion scope)
		nodeObj.right = self.buildTreePost(division+1,end)
		nodeObj.left  = self.buildTreePost(begin,division-1)

		return nodeObj

	def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
		self.I=inorder
		self.P=postorder
		self.buildIndex=len(postorder)-1
		root = self.buildTreePost(0,self.buildIndex)
		return root