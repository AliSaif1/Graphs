class WeightedGraph:
    def __init__(self):
        self.graph = {}
        self.weights = {}

    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def addEdge(self, node1, node2, weight):
        self.addNode(node1)
        self.addNode(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        self.weights[(node1, node2)] = weight
        self.weights[(node2, node1)] = weight

    def getNode(self, node):
        return self.graph[node]

    def __str__(self):
        return str(self.graph)
