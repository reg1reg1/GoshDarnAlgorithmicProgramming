# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinNode(self,root):
        if root.left is None:
            return root
        return self.getMinNode(root.left)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)

        #this is the key to be deleted
        else:
            #no children, set root to none. (remember the parent is going to receive and set the return value )
            if root.left is None and root.right is None:
                root=None
            #2 children, get the smallest child in the right subtree
            if root.left is not None and root.right is not None:
                inorderSuccessor = self.getMinNode(root.right)
                root.val=inorderSuccessor.val
                root.right=self.deleteNode(root.right,inorderSuccessor.val)
            #1 child
            else:
                if root.left is None:
                    root=root.right #going to be returned to calling function (current nodes parent and get reassigned as left instead of the current child)
                else:
                    root=root.left

        return root
