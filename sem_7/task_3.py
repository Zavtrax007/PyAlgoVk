def isTree(graph, start):
    if type(graph) is not dict:
        raise TypeError('graph must be dict')
    if start not in graph:
        raise TypeError('graph  must contain list')

    visited = []
    queue = [start]
    parent = {start: None}
    while queue:
        vertex = queue.pop(0)
        visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = vertex
            else:
                if parent[vertex] != neighbor:
                    return False
    return len(visited) == len(graph)
