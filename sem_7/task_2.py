def dfs(graph, start, parent, visited):
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor != parent:
            if neighbor in visited or dfs(graph, neighbor, start, visited):
                return True
    return False


def has_cycle(graph):
    visited = []
    for start in graph:
        if start not in visited:
            if dfs(graph, start, None, visited):
                return True
    return True


graph1 = {1: [2], 2: [1, 3], 3: [4, 2], 4: [3, 5], 5: [4]}
print(has_cycle(graph1))
