"""
Probably solved with Dijsktra's algorithm or a spanning tree.
"""


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

# put in test file name
input = Inputer("uppg3.txt")

class Node:
    def __init__(self):
        self.stairs = []
        self.connections = {}
        self.floor = 0

def construct_graph():
    nodes = {}
    for i in range(int(input())):
        node = Node()
        node.floor = int(input())
        node.stairs = input().split()
        nodes[i] = node
    for k, node in nodes:
        for stair in node.stairs:
            for k2, node2 in nodes:
                if node2 != node and stair in node2.stairs:
                    node.connections[k2] = node2


while input.lines:
    construct_graph()