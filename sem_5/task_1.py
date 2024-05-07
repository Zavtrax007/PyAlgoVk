from Tree_al import Node, dept_traversal


def buildTree(arr, i):
    if type(arr) is not list:
        raise TypeError('Array must be list')
    if type(i) is not int:
        raise TypeError('Iterator must be integer')
    if i >= len(arr):
        return None
    root = Node(arr[i])
    root.left = buildTree(arr, 2 * i + 1)
    root.right = buildTree(arr, 2 * i + 2)
    return root



