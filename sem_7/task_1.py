def dfs(graph, start, visited, color):
    visited[start] = color
    for neighbor in graph[start]:
        if visited[start] == 0:
            dfs(graph, neighbor, visited, color)


def find_connected_comp(graph):
    visited = {}
    for i in range(len(graph)+1):
        visited[i] = 0
    color = 0
    for node in graph:
        if visited[node] == 0:
            color += 1
            dfs(graph, node, visited, color)
    return visited


graph = {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [5], 5: [4]}
print(find_connected_comp(graph))