def countNodes(node):
    if node is None:
        return 0
    else:
        return (1+countNodes(node.left)+countNodes(node.right))
        
def isComplete(root,index,number):
    
    if root is None:
        return True
    
    if index>=number:
        return False
    else:
        return isComplete(root.left,2*index+1,number) and isComplete(root.right,2*index+2,number)
        
    
def isMaxHeap(root):
    if root is None:
        return True
    if root.left is not None:
        if root.data< root.left.data:
            return False
    if root.right is not None:
        if root.data < root.right.data:
            return False
    return isMaxHeap(root.left) and isMaxHeap(root.right)
        
def isHeap(root):
    number_node=countNodes(root)
    return isComplete(root,0,number_node) and isMaxHeap(root)