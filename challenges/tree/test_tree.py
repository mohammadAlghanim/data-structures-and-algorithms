import pytest
from challenges.tree.main_tree import Tree
from challenges.tree.main_tree import Node
from challenges.tree.main_tree import Binary_Search_Tree
def test_Binary_Search_Tree():
    # Create the tree and build its structure
    bst = Binary_Search_Tree()
    bst.add_binary_search(bst.root,5)
    bst.add_binary_search(bst.root,3)
    bst.add_binary_search(bst.root,7)
    bst.add_binary_search(bst.root,2)
    bst.add_binary_search(bst.root,4)
    
    # Perform post_order traversal
    result1 = bst.pre_order(bst.root,list =[])

    # Define the expected result
    expected2 = [5, 3, 2, 4, 7]
    assert expected2 == result1

def test_pre_order():
    # Create the tree and build its structure
    tree = Tree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("k")
    tree.root.right.right = Node("g")
    
    # Perform pre-order traversal
    result = tree.pre_order(tree.root)

    # Define the expected result
    expected = ['A', 'B', 'D', 'E', 'C', 'k', 'g']
    

    # Compare the expected result with the actual result
    assert expected == result
def test_in_order():
    # Create the tree and build its structure
    tree2 = Tree()
    tree2.root = Node("A")
    tree2.root.left = Node("B")
    tree2.root.right = Node("C")
    tree2.root.left.left = Node("D")
    tree2.root.left.right = Node("E")
    tree2.root.right.left = Node("k")
    tree2.root.right.right = Node("g")
    
    # Perform in_order traversal
    result = tree2.in_order(tree2.root)

    # Define the expected result
    expected = "['D', 'B', 'E', 'A', 'k', 'C', 'g']"

    # Compare the expected result with the actual result
    assert expected == str(result)
def test_post_order():
    # Create the tree and build its structure
    tree3 = Tree()
    tree3.root = Node("A")
    tree3.root.left = Node("B")
    tree3.root.right = Node("C")
    tree3.root.left.left = Node("D")
    tree3.root.left.right = Node("E")
    tree3.root.right.left = Node("k")
    tree3.root.right.right = Node("g")
    
    # Perform post_order traversal
    result = tree3.post_order(tree3.root)

    # Define the expected result
    expected = ['D', 'E', 'B', 'k', 'g', 'C', 'A']

    # Compare the expected result with the actual result
    assert expected == result
