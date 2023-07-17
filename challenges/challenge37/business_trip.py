from graph import Graph
from Node import Node 


# class Edge:
#     def __init__(self, vertex, weight=0):
#         """
#         Initialize an Edge object.

#         Args:
#             vertex: The vertex (Node object) connected by the edge.
#             weight (optional): The weight of the edge (default is 0).
#         """
#         self.vertex = vertex
#         self.weight = weight

#     def __repr__(self):
#         """
#         Return a string representation of the Edge object.
#         """
#         return f"{self.vertex} (Weight: {self.weight})"


# class Graph:
#     def __init__(self):
#         self.adj_list = {}

#     def add_node(self, value):
#         new_vertex = Node(value)
#         self.adj_list[new_vertex] = []
#         return new_vertex

#     def add_edge(self, node1, node2, weight=0):
#         edge1 = Edge(node2, weight)
#         self.adj_list[node1].append(edge1)

#         # For directed graph, add both directions for the edge
#         edge2 = Edge(node1, weight)
#         self.adj_list[node2].append(edge2)

# # ... (rest of the code as before)


# # ... (rest of the code as before)


#     def get_vertices(self):
#         """
#         Get all the vertices in the graph.

#         Returns:
#             A list of all the vertices in the graph.
#         """
#         return list(self.adj_list.keys())

#     def get_neighbors(self, vertex):
#         """
#         Get the neighbors of a given vertex.

#         Args:
#             vertex: The vertex (Node object) for which to find neighbors.

#         Returns:
#             A list of Edge objects representing the neighbors of the vertex.
#         """
#         if vertex not in self.adj_list.keys():
#             return []

#         return self.adj_list[vertex]

#     def size(self):
#         """
#         Get the total number of vertices in the graph.

#         Returns:
#             The total number of vertices in the graph.
#         """
#         return len(self.adj_list)

#     def breadth_first(self, root):
#         '''
#         A method that takes a value as an argument, then traverses through the graph using Breadth-First way starting from the inputted value,
#         and appends all the visited nodes' values in a returned array.
#         '''
#         nodes = []
#         breadth = Queue()
#         visited = set()

#         breadth.enqueue(root)
#         visited.add(root)

#         while not breadth.is_empty():
#             front = breadth.dequeue()
#             nodes.append(front.value)

#             for edge in self.adj_list[front]:
#                 if edge.vertex not in visited:
#                     breadth.enqueue(edge.vertex)
#                     visited.add(edge.vertex)

#         return nodes
#     def __str__(self):
#         """
#         Return a string representation of the Graph object.
#         """
#         output = ''
#         for vertex in self.adj_list.keys():
#             output += f'{vertex} -> '
#             for edge in self.adj_list[vertex]:
#                 output += f'{edge.vertex} -----> '
#             output += '\n'
#         return output
    
    

def business_trip(graph, cities):
    """
    Calculate the total cost of a trip based on direct flights between cities.

    Args:
        graph (Graph): The graph object representing the flights between cities.
        cities (list): A list of Node objects representing the cities in the trip.

    Returns:
        int: The total cost of the trip if it's possible with direct flights, None otherwise.
    """
    if not cities:
        return None

    cost = 0

    for i in range(len(cities) - 1):
        current_city = cities[i]
        next_city = cities[i + 1]

        # Check if both current_city and next_city exist in the graph
        if current_city not in graph.adj_list or next_city not in graph.adj_list:
            return None

        # Check if there is a direct flight between current_city and next_city
        direct_flight = False
        for edge in graph.adj_list[current_city]:
            if edge.vertex == next_city:
                cost += edge.weight
                direct_flight = True
                break

        if not direct_flight:
            return None

    return cost


# Rest of the code as before

if __name__ == "__main__":
    graph = Graph()
    node_metroville = graph.add_node('Metroville')
    node_pandora = graph.add_node('Pandora')
    node_arendelle = graph.add_node('Arendelle')
    node_monstropolis = graph.add_node('Monstropolis')

    graph.add_edge(node_metroville, node_pandora, 82)
    graph.add_edge(node_metroville, node_arendelle, 99)
    graph.add_edge(node_metroville, node_monstropolis, 105)
    graph.add_edge(node_pandora, node_arendelle, 42)
    graph.add_edge(node_arendelle, node_monstropolis, 73)
    graph.add_edge(node_monstropolis, node_pandora, 26)

    cities_trip = [node_metroville, node_pandora]
    total_cost = business_trip(graph, cities_trip)

    if total_cost is not None:
        print(f"The total cost of the trip is ${total_cost}.")
    else:
        print("The trip is not possible.")




# if __name__ == "__main__":
#     graph = Graph()
#     node_seattle = graph.add_node('Seattle')
#     node_new_york = graph.add_node('New York')
#     node_los_angeles = graph.add_node('Los Angeles')

#     graph.add_edge(node_seattle, node_new_york, 300)
#     graph.add_edge(node_seattle, node_los_angeles, 150)
#     graph.add_edge(node_new_york, node_los_angeles, 250)

#     cities_trip = [node_seattle, node_los_angeles, node_new_york]

#     total_cost = business_trip(graph, cities_trip)

#     if total_cost is not None:
#         print(f"The total cost of the trip is ${total_cost}.")
#     else:
#         print("The trip is not possible.")

    
  
        



