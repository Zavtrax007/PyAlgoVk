class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)


def dept_traversal(root, res):
    if root is None:
        return
    dept_traversal(root.left, res)
    res.append(root.data)
    dept_traversal(root.right, res)
    return res


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
