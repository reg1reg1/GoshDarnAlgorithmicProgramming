# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		if root==p or root==q:
			return root
		

		node_l = self.lowestCommonAncestor(root.left,p,q)
		node_r = self.lowestCommonAncestor(root.right,p,q)


		#if both queries return value then both p and q are present on either side of the current node, making this node the LCA
		if node_l and node_r:
			return root

		#if node_l exists and node_r does not, both nodes exist in the left side of the 
		if node_l:
			return node_r
		else:
			return node_l
			
