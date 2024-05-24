def dfs(graph, start, visited, color):
    visited[start] = color
    for neighbor in graph[start]:
        if visited[neighbor] == 0:
            dfs(graph, neighbor, visited, color)


def findConnectedComp(graph):
    if type(graph) is not dict:
        raise TypeError('graph  must be dict')
    visited = {}
    for i in graph:
        visited[i] = 0
    color = 0
    for node in graph:
        if visited[node] == 0:
            color += 1
            dfs(graph, node, visited, color)
    return visited



