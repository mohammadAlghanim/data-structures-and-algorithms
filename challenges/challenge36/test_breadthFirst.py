import pytest

from challenges.challenge36.graph import Graph

# Helper function to create a graph for testing
def test_graph_breadth_first():
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

    assert graph1.breadth_first(a) == ['A', 'B', 'C', 'D']

def test_breadth_first():
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
    assert graph1.breadth_first(c) == ['C', 'A', 'B', 'D']