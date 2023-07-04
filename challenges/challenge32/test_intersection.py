import pytest
from tree import Tree, Node
from Hashtable import HashTable
from tree_intersection import tree_intersection

def test_tree_intersection():
    # Create tree1
    tree1 = Tree()
    tree1.root = Node(5)
    tree1.root.left = Node(3)
    tree1.root.right = Node(7)
    tree1.root.left.left = Node(2)
    tree1.root.left.right = Node(4)

    # Create tree2
    tree2 = Tree()
    tree2.root = Node(1)
    tree2.root.left = Node(3)
    tree2.root.right = Node(6)
    tree2.root.left.left = Node(4)
    tree2.root.left.right = Node(7)

    # Call the tree_intersection function
    result = tree_intersection(tree1, tree2)

    # Assert the expected result
    assert result == {3, 4, 7}
