from Tree_al import Node, dept_traversal
from task_1 import buildTree


def isSymetricDFS(root):
    if type(root) is not Node:
        raise TypeError('root must be Node')
    if root is None:
        return True
    data = []
    dept_traversal(root, data)
    j = len(data) - 1
    for i in range(len(data) // 2):
        if data[i] != data[j]:
            return False
        j -= 1
    return True
