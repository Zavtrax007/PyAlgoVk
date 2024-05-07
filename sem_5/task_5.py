from Tree_al import Node, dept_traversal


def isSameTree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if type(a) is not Node and type(a) is not True and type(a) is not False:
        raise TypeError('a and b must be Nodes')
    if type(b) is not Node and type(b) is not True and type(b) is not False:
        raise TypeError('a and b must be Nodes')
    if a.data != b.data:
        return False
    return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
