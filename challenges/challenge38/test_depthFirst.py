import pytest

from challenges.challenge38.graph import Graph

# Helper function to create a graph for testing
def test_graph_depth_first():
    graph = Graph()
    # Add nodes
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    node4 = graph.add_node(4)
    node5 = graph.add_node(5)
    # Add edges
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node3)
    graph.add_edge(node2, node4)
    graph.add_edge(node2, node5)

    assert graph.depth_first(node1) == [1, 2, 4, 5, 3]

