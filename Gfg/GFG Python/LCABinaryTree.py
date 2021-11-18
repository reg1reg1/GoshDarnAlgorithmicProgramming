def lca(root, n1, n2):
    if root is None:
        return
    if root.data == n1 or root.data == n2:
        return root
    node_left = lca(root.left,n1,n2)
    node_right = lca(root.right,n1,n2)
    
    if node_left is not None and node_right is not None:
        return root
    else:
        if node_left is None:
            return node_right
        else:
            return node_left