def find_max_path_sum(root):
    max_sum = 0
    max_path = []

    def dfs(node):
        if node is None:
            return 0, []
        left_sum, left_path = dfs(node.left)
        right_sum, right_path = dfs(node.right)
        if left_sum < right_sum:
            current_max_path = left_path + [node.data]
        else:
            current_max_path = right_path + [node.data]

        current_max_sum = max(left_sum, right_sum) + node.data
        if left_sum + node.data + right_sum > max_sum:
            max_sum = left_sum + node.data + right_sum
            max_path = left_path + [node.data] + right_path

        return current_max_sum, current_max_path
