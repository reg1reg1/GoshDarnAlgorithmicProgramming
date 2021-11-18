def isIdentical(r1, r2):
    bool x
    if r1 is None and r2 is not None:
        return False
    if r1 is not None and r2 is None:
        return False
    if r1.data!=r2.data:
        return False
    if r1.data==r2.data:
        return isIdentical(r1.left,r2.left) and isIdentical(r1.right,r2.right)