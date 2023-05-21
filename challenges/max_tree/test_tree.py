import pytest
from challenges.max_tree.main_tree import Tree
from challenges.max_tree.main_tree import Node
from challenges.max_tree.main_tree import Binary_Search_Tree
def test_Binary_Sear_maximum_value():
    bst = Binary_Search_Tree()
    bst.add_binary_search(bst.root,5)
    bst.add_binary_search(bst.root,3)
    bst.add_binary_search(bst.root,7)
    bst.add_binary_search(bst.root,2)
    bst.add_binary_search(bst.root,4)

    result1 = bst.find_maximum_value()

    expected2 = 7
    assert expected2 == result1

def test_pre_order():
    tree1 = Tree()

    node1 = Node(5)
    tree1.root = node1

    node2 = Node(4)
    tree1.root.left = node2

    node3 = Node(9)
    tree1.root.right = node3

    node4 = Node(12)
    tree1.root.left.left = node4

    node5 = Node(6)
    tree1.root.left.right = node5

    node6 = Node(15)
    tree1.root.right.left = node6
   
    result = tree1.find_maximum_value()

    expected = 15
 
    assert expected == result
def test_in_order():
    
    tree2 = Tree()
    tree2.root = Node(3)
    tree2.root.left = Node(9)
    tree2.root.right = Node(10)
    tree2.root.left.left = Node(7)
    tree2.root.left.right = Node(8)
    tree2.root.right.left = Node(7)
    tree2.root.right.right = Node(5)

    result = tree2.max_tree(tree2.root)

    expected = 10

    assert expected == result
