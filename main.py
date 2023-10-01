from DirectedGraph import DirectedGraph
from graph import Graph
from directed_Weighted_Graph import DirectedWeightedGraph
from weightedGraph import WeightedGraph

undirected_graph = Graph()

undirected_graph.addEdge('A', 'B')
undirected_graph.addEdge('A', 'D')
undirected_graph.addEdge('B', 'C')
undirected_graph.addEdge('B', 'D')
undirected_graph.addEdge('C', 'D')

print("Undirected graph: ")
print(undirected_graph.getNode('A'))
print(undirected_graph)

directed_graph = DirectedGraph()

directed_graph.addEdge('A', 'B')
directed_graph.addEdge('A', 'D')
directed_graph.addEdge('B', 'C')
directed_graph.addEdge('B', 'D')
directed_graph.addEdge('C', 'D')

print("directed graph: ")
print(directed_graph.getNode('A'))
print(directed_graph)

weighted_graph = WeightedGraph()

weighted_graph.addEdge('A', 'B', 1)
weighted_graph.addEdge('A', 'D', 2)
weighted_graph.addEdge('B', 'C', 2)
weighted_graph.addEdge('B', 'D', 5)
weighted_graph.addEdge('C', 'D', 3)

print("Undirected Weighted graph: ")
print(weighted_graph.getNode('A'))
print(weighted_graph)
print(weighted_graph.weights)

directed_weighted_graph = DirectedWeightedGraph()

directed_weighted_graph.addEdge('A', 'B', 1)
directed_weighted_graph.addEdge('A', 'D', 2)
directed_weighted_graph.addEdge('B', 'C', 2)
directed_weighted_graph.addEdge('B', 'D', 5)
directed_weighted_graph.addEdge('C', 'D', 3)

print("directed Weighted graph: ")
print(directed_weighted_graph.getNode('A'))
print(directed_weighted_graph)
print(directed_weighted_graph.weights)
