from Tree_al import Node, dept_traversal


def minDept(root):
    if type(root) is not Node and root is not None:
        raise TypeError('root must be Node')
    if root is None:
        return 0
    if root.left is not None and root.right is not None:
        return 1 + min(minDept(root.left), minDept(root.right))
    if root.left is None:
        return 1 + minDept(root.left)
    if root.right is None:
        return 1 + minDept(root.right)
