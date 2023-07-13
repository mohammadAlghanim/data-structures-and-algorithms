import pytest
from graph import Graph

def test_graph():
    # Create a graph
    graph = Graph()

    # Add nodes
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')

    # Test get_vertices method
    vertices = graph.get_vertices()
    expected = '[A, B, C]'
    assert expected == str(vertices)
    assert graph.size() == 3
def test_graph_2():
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

    assert  graph1




  
    

 

