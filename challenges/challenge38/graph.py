from Node import Node
from Queue import Queue

class Edge:
    def __init__(self, vertex, weight=0):
        """
        Initialize an Edge object.

        Args:
            vertex: The vertex (Node object) connected by the edge.
            weight (optional): The weight of the edge (default is 0).
        """
        self.vertex = vertex
        self.weight = weight

    def __repr__(self):
        """
        Return a string representation of the Edge object.
        """
        return f"{self.vertex} (Weight: {self.weight})"


class Graph:
    def __init__(self):
        """
        Initialize a Graph object.
        """
        self.adj_list = {}

    def add_node(self, value):
        """
        Add a new node to the graph.

        Args:
            value: The value of the node.

        Returns:
            The newly created Node object.
        """
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self, node1, node2, weight=0):
        """
        Add an edge between two nodes in the graph.

        Args:
            node1: The first node (Node object).
            node2: The second node (Node object).
            weight (optional): The weight of the edge (default is 0).

        Returns:
            None if the nodes exist, otherwise returns a message indicating that the node(s) do not exist.
        """
        if node1 not in self.adj_list.keys() or node2 not in self.adj_list.keys():
            return "This node does not exist"

        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def get_vertices(self):
        """
        Get all the vertices in the graph.

        Returns:
            A list of all the vertices in the graph.
        """
        return list(self.adj_list.keys())

    def get_neighbors(self, vertex):
        """
        Get the neighbors of a given vertex.

        Args:
            vertex: The vertex (Node object) for which to find neighbors.

        Returns:
            A list of Edge objects representing the neighbors of the vertex.
        """
        if vertex not in self.adj_list.keys():
            return []

        return self.adj_list[vertex]

    def size(self):
        """
        Get the total number of vertices in the graph.

        Returns:
            The total number of vertices in the graph.
        """
        return len(self.adj_list)

    def breadth_first(self, root):
        '''
        A method that takes a value as an argument, then traverses through the graph using Breadth-First way starting from the inputted value,
        and appends all the visited nodes' values in a returned array.
        '''
        nodes = []
        breadth = Queue()
        visited = set()

        breadth.enqueue(root)
        visited.add(root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            nodes.append(front.value)

            for edge in self.adj_list[front]:
                if edge.vertex not in visited:
                    breadth.enqueue(edge.vertex)
                    visited.add(edge.vertex)

        return nodes
    def depth_first(self, start_node):
        """
        Perform a depth-first traversal starting from the given node.

        Args:
            start_node: The starting node (Node object) for the depth-first traversal.

        Returns:
            A list of Node objects representing the nodes in their pre-order depth-first traversal order.
        """
        visited = set()
        result = []

        def dfs_helper(node):
            if node is None:
                return

            visited.add(node)
            result.append(node.value)

            for edge in self.adj_list[node]:
                if edge.vertex not in visited:
                    dfs_helper(edge.vertex)

        dfs_helper(start_node)
        return result
    def __str__(self):
        """
        Return a string representation of the Graph object.
        """
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output
    
    