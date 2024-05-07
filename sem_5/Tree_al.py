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



