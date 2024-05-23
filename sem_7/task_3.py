def is_tree(graph, start):
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


gr = {1: [2, 3, 4], 2: [1], 3: [1], 4: [1, 5, 6], 5: [4], 6: [4]}
print(is_tree(gr, gr[1][0]))
