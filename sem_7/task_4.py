def dijksta(graph, start):
    if type(graph) is not dict:
        raise TypeError('graph must be dict')
    if start not in graph:
        raise TypeError('graph must contain start')
    inf = float('inf')
    visited = {}
    for vertex in graph:
        visited[vertex] = False
    dist = {}
    for vertex in graph:
        dist[vertex] = inf
    dist[start] = 0

    def vertexWithMinWeight(graph, visited):
        index = ''
        dist_min = float('inf')
        for vert in graph:
            if dist[vert] < dist_min and visited[vert] is False:
                dist_min = dist[vert]
                index = vert
        return index

    while False in visited.values():
        u = vertexWithMinWeight(graph, visited)
        for v in graph[u]:
            if graph[u][v] != 0 and visited[v] is False:
                dist[v] = min(dist[v], dist[u] + graph[u][v])
        visited[u] = True
    return dist



