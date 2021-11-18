# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def utilSum(self,node,ans):
        if node is not None:
            ans=ans*10+node.val
            if node.left is None and node.right is None:
                self.tot+=ans
                #print(self.tot)
            else:
                self.utilSum(node.left,ans)
                self.utilSum(node.right,ans)
                
    def sumNumbers(self, root: TreeNode) -> int:
        self.tot=0
        self.utilSum(root,0)
        return self.tot