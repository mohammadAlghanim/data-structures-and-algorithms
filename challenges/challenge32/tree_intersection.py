from tree import Tree , Node
from Hashtable import HashTable

def tree_intersection(tree1, tree2):
    """
    Finds the intersection of values between two binary trees.

    Args:
        tree1 (Tree): The first binary tree.
        tree2 (Tree): The second binary tree.

    Returns:
        set: A set of values found in both trees.

    Algorithm:
    1. Create an empty set called `values_set`.
    2. Traverse the first tree (tree1) and store all values in a hash table.
    3. Traverse the second tree (tree2) and check if each value exists in the hash table.
       If it does, add the value to the `values_set`.
    4. Return the `values_set` containing the intersection of values.

    Example:
        tree1:
                 5
               /   \
              3     7
             / \
            2   4

        tree2:
                 1
               /   \
              3     6
             / \
            4   7

        The intersection of values between tree1 and tree2 is {3, 4, 7}.
    """
    values_set = set()

    # Traverse the first tree and store all values in a hash table
    hash_table = HashTable()
    for value in tree1.in_order(tree1.root):
        hash_table.set(value, True)

    # Traverse the second tree and check if each value exists in the hash table
    for value in tree2.in_order(tree2.root):
        if hash_table.has(value):
            values_set.add(value)

    return values_set

if __name__ == "__main__":
    tree1 = Tree()

    # Add elements to tree1
    tree1.root = Node(5)
    tree1.root.left = Node(3)
    tree1.root.right = Node(7)
    tree1.root.left.left = Node(2)
    tree1.root.left.right = Node(4)

    tree2 = Tree()

    # Add elements to tree2
    tree2.root = Node(1)
    tree2.root.left = Node(3)
    tree2.root.right = Node(6)
    tree2.root.left.left = Node(4)
    tree2.root.left.right = Node(7)

    result = tree_intersection(tree1, tree2)
    print(result)
