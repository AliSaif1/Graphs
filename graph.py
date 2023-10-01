class Graph:
    def __init__(self):
        self.graph = {}

    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def addEdge(self, node1, node2):
        self.addNode(node1)
        self.addNode(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def getNode(self, node):
        return self.graph[node]

    def __str__(self):
        return str(self.graph)
