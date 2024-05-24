def dfs(graph, start, parent, visited):
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor != parent:
            if neighbor in visited or dfs(graph, neighbor, start, visited):
                return True
    return False


def hasCycle(graph):
    if type(graph) is not dict:
        raise TypeError('graph must be dict')
    visited = []
    for start in graph:
        if start not in visited:
            if dfs(graph, start, None, visited):
                return True
    return False


