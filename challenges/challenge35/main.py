from graph import Graph

graph1 = Graph()

a = graph1.add_node('A')
b = graph1.add_node('B')
c = graph1.add_node('C')
d = graph1.add_node('D')

graph1.add_edge(a, b)
graph1.add_edge(a, c)
graph1.add_edge(c, b)
graph1.add_edge(d, b)
graph1.add_edge(d, c)

print(graph1)
# Testing the get_vertices method
vertices = graph1.get_vertices()
print("Vertices:", vertices)

# Testing the get_neighbors method
for vertex in vertices:
    neighbors = graph1.get_neighbors(vertex)
    print("Neighbors of", vertex, ":", neighbors)

# Testing the size method
graph_size = graph1.size()
print("Graph size:", graph_size)

