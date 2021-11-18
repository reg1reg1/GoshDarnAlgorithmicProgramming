# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
from collections import deque
class Solution:
	def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
		q=deque()
		q.append((root,0,None))
		f1=False
		f2=False
		xParent=None
		yParent=None
		xLevel=None
		yLevel=None

		if root.val == x or root.val == y:
			return False

		while len(q)!=0:
			x=q.popleft()
			
			#parent of the children being pushed will be the node which got popped
			parent=x[0]
			
			#push the children into the queue
			if x[0].left is not None:
				if x[0].left.val == x:
					f1 = True
					xParent=parent
					xLevel=x[1]+1
				elif x[0].left.val==y:
					f2=True
					yParent=parent
					yLevel=x[1]+1
				q.append((x[0].left,x[1]+1,parent))

			if x[0].right is not None:
				if x[0].right.val == x:
					f1 = True
					xParent=parent
					xLevel=x[1]+1
				elif x[0].right.val==y:
					f2=True
					yParent=parent
					yLevel=x[1]+1
				q.append((x[0].right,x[1]+1,parent))

			#found both
			if f1 and f2:
				break
		
		if xParent!=yParent and xLevel == yLevel:
			return True
		return False