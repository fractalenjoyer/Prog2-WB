class Inputer:
    def __init__(self, file):
        with open(file, "r") as f:
            self.lines = [line.strip() for line in f][::-1]
        self.remaining = len(self.lines)

    def __call__(self, *args):
        if self.remaining  == 0:
            return None
        self.remaining -= 1
        return self.lines.pop()

import numpy as np
from collections import deque
from itertools import combinations

class Node:
    def __init__(self):
        self.name = None
        self.level = None
        self.connections = []
        self.edges = ""

    def __repr__(self):
        return f"Node({self.name}, {self.level}, {self.connections})"

    def get_weight(self, node):
        return abs(self.level - node.level)


def construct_graph(nodes):
    graph = [Node() for i in range(len(nodes))]
    for k, v in enumerate(nodes):
        graph[k].name = k
        graph[k].level = v[0]
        graph[k].edges = set(v[1])
    for i, j in combinations(graph, 2):
        if i.edges & j.edges:
            i.connections.append(j)
            j.connections.append(i)
    return graph

def dijkstra(graph, start):
    heap = deque([graph[start]])
    dist = np.full(len(graph), np.inf)
    dist[graph[start].name] = 0
    while heap:
        v = heap.pop()
        for u in v.connections:
            if dist[u.name] > dist[v.name] + v.get_weight(u):
                dist[u.name] = dist[v.name] + v.get_weight(u)
                heap.append(u)
    return dist

def visit_all(graph, start):
    visited = np.zeros(len(graph), dtype=float)
    visited[start] = np.inf
    dist = 0
    nxt = start
    while np.min(visited) != np.inf:
        dists = dijkstra(graph, nxt)
        nxt = np.argmin(dists + visited)
        visited[nxt] = np.inf
        dist += dists[nxt]
    return dist


def main():
    nodes = []
    for i in range(int(input())):
        nodes.append([int(input()), input()])

    graph = construct_graph(nodes)

    print("Svar:", int(sum([dijkstra(graph, i)[i+1]
          for i in range(len(graph)-1)])))


# put in test file name
input = Inputer("uppg3.txt")

while input.lines:
    main()