from graph import Graph
graph = Graph()

node1 = graph.add_node(1)
node2 = graph.add_node(2)
node3 = graph.add_node(3)
node4 = graph.add_node(4)
node5 = graph.add_node(5)

graph.add_edge(node1, node2)
graph.add_edge(node1, node3)
graph.add_edge(node2, node4)
graph.add_edge(node2, node5)

print(graph.depth_first(node1)) 


