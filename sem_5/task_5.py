from Tree_al import Node, dept_traversal


def isSameTree(a, b):
    if type(a) is not Node or type(b) is not Node:
        raise TypeError('a and b must be Nodes')
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.data != b.data:
        return False
    return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
