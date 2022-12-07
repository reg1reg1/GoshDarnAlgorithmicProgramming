# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #reverseinordertraversal
    def revIT(self,root):
        if root is None:
            return
        
        if root.right:
            self.revIT(root.right)
        
        
        #if p2 is unset after this function ends, set p2 to the last_node visited
        self.node_visited=root
        #print(root.val,end=" ")
        if self.prev is None:
            self.prev=root
        else:
            if self.p1 is None:
                
                #the first element out of order prev must always be greater in value than current (reverse inorder) , we mark the previous node as the violating entity here
                if root.val>self.prev.val:
                    #print("\nSetting P1")
                    self.p1=self.prev
                    #print("P1 value ",self.p1.val)
            else:
                #we traverse from current and travel till we find a node whose value is less than p1. The previous of that node will be the violating entity
                if self.p1.val > root.val and self.p2 is None:
                    #print("Setting P2",self.prev.val,"CURR ",root.val)
                    self.p2=self.prev
        
        if self.p1 is not None and self.p2 is not None:
            return
        self.prev=root


        if root.left:
            self.revIT(root.left)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev=None
        self.p1=None
        self.p2=None
        self.revIT(root)
        #print("\n\n\n")
        if self.p2 is None:
            self.p2=self.node_visited
        #print(self.p1.val,self.p2.val)
        self.p1.val,self.p2.val=self.p2.val,self.p1.val
        #self.revIT(root)
        return