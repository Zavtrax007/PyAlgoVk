import sys


def vertexWithMinWeight():
    index = ''
    dist_min = 0


def dijksta(graph, start):
    inf = sys.maxsize
    visited = {}
    for vertex in range(graph):
        visited[vertex] = False
    dist = {}

    gr = {'a': {'b': 1, 'c': 5}, 'b': {'a': 1, 'c': 2, 'd': 3}, 'c': {'a': 5, 'b': 2, 'd': 1}, 'd': {'c': 1, 'b': 3}}
