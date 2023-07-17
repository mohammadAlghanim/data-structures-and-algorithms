import pytest
from graph import Graph
from business_trip import business_trip

def test_business_trip_direct_flights():
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

    # Test case 1: Direct flights from Metroville to Pandora
    cities_trip = [node_metroville, node_pandora]
    assert business_trip(graph, cities_trip) == 82

    # Test case 2: Direct flights from Metroville to Arendelle
    cities_trip = [node_metroville, node_arendelle]
    assert business_trip(graph, cities_trip) == 99

    # Test case 3: Direct flights from Pandora to Arendelle
    cities_trip = [node_pandora, node_arendelle]
    assert business_trip(graph, cities_trip) == 42

def test_business_trip_with_layover():
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

    # Test case 4: Trip with a layover from Metroville to Monstropolis via Pandora
    cities_trip = [node_metroville, node_pandora, node_monstropolis]
    assert business_trip(graph, cities_trip) == 82 + 26

def test_business_trip_not_possible():
    graph = Graph()
    node_metroville = graph.add_node('Metroville')
    node_pandora = graph.add_node('Pandora')
    node_arendelle = graph.add_node('Arendelle')
    node_monstropolis = graph.add_node('Monstropolis')

    graph.add_edge(node_metroville, node_pandora, 82)
    graph.add_edge(node_metroville, node_arendelle, 99)
    graph.add_edge(node_pandora, node_arendelle, 42)
    graph.add_edge(node_arendelle, node_monstropolis, 73)

    # Test case 5: No direct flight from Metroville to Monstropolis
    cities_trip = [node_metroville, node_monstropolis]
    assert business_trip(graph, cities_trip) is None

    # Test case 6: Direct flight from Arendelle to Pandora
    cities_trip = [node_arendelle, node_pandora]
    assert business_trip(graph, cities_trip) == 42

    # Test case 7: Direct flight from Pandora to Arendelle
    cities_trip = [node_pandora, node_arendelle]
    assert business_trip(graph, cities_trip) == 42

    # Test case 8: No direct flight from Monstropolis to Metroville
    cities_trip = [node_monstropolis, node_metroville]
    assert business_trip(graph, cities_trip) is None



