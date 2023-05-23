import pytest
from challenges.challenge17.tree_breadth_first import Node
from challenges.challenge17.tree_breadth_first import Tree_breadth_first
def test_breadth_1():
    tree1 = Tree_breadth_first()
    tree1.insert(2)
    tree1.insert(8)
    tree1.insert(74)
    tree1.insert(7)
    tree1.insert(10)
    tree1.insert(6)
    tree1.insert(8)
    result1 = tree1.breadth_first()
    expected = [2, 8, 74, 7, 10, 6, 8]
    assert expected == result1
def test_breadth_2():
    tree1 = Tree_breadth_first()
    tree1.insert(2)
    tree1.insert(74)
    tree1.insert(8)
    
    result1 = tree1.breadth_first()
    expected = [2, 74, 8]
    assert expected == result1

