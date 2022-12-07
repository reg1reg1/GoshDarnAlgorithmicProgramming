# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        _stacklist=[]
        _stacklist.append(root)
        top=0
        current = root.left
        while True:
            if current is not None:
                _stacklist.append(current)
                current = current.left
                top+=1
            elif len(_stacklist)!=0:
                current = _stacklist.pop()
                top-=1
                output.append(current.val)
                current = current.right
            else:
                break

