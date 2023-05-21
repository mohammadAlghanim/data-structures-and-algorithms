class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    """
        Initializes an instance of the Tree class.

        The root of the tree is set to None upon initialization.

    """
    def __init__(self):
        self.root = None
        
    """
        Traverses the tree in pre-order and returns a list of values.

        Pre-order traversal visits the root node first, then the left subtree,
        and finally the right subtree.

        Args:
            root: The root node of the tree.
            list: (optional) A list to store the visited values.

        Returns:
            A list containing the values of the tree nodes visited in pre-order.

    """
    def pre_order(self, root,list=None):
        if list == None:
            list = []
        if root is not None:
            # print(root.value)
            list.append(root.value)
            self.pre_order(root.left,list)
            self.pre_order(root.right,list)
        return list
    """
        Traverses the tree in in-order and returns a list of values.

        In-order traversal visits the left subtree first, then the root node,
        and finally the right subtree.

        Args:
            root: The root node of the tree.
            list: (optional) A list to store the visited values.

        Returns:
            A list containing the values of the tree nodes visited in in-order.

    """
    def in_order(self,root,list =None):
        if list == None:
            list = []
        if root.left is not None:
          self.in_order(root.left,list)
        if root is not None:
          list.append(root.value)
        #   print(root.value)
        if root.right is not None:
          self.in_order(root.right,list)
        return list
    """
        Traverses the tree in post-order and returns a list of values.

        Post-order traversal visits the left subtree first, then the right subtree,
        and finally the root node.

        Args:
            root: The root node of the tree.
            list: (optional) A list to store the visited values.

        Returns:
            A list containing the values of the tree nodes visited in post-order.

    """
    def post_order(self,root,list=None):
        if list == None:
            list = []

        if root is not None:
            # print(root.value)
            self.post_order(root.left,list)
            self.post_order(root.right,list)
            list.append(root.value)
        return list
    

    def find_maximum_value(self):
        """
        Finds the maximum value stored in the binary tree.

        Returns:
            The maximum value stored in the binary tree, or None if the tree is empty.
        """
        if self.root is None:
            return None

        return self.max_tree(self.root)
    def max_tree(self, root):
       """
        Recursive helper method to find the maximum value in a binary tree.

        Args:
            root (Node): The root node of the binary tree.

        Returns:
            The maximum value in the binary tree, or None if the tree is empty.
        """
       if root is None:
          return None

       max_num = root.value

       right_max = self.max_tree(root.right)
       if right_max is not None and max_num < right_max:
          max_num = right_max

       left_max = self.max_tree(root.left)
       if left_max is not None and max_num < left_max:
          max_num = left_max

       return max_num
###########
class Binary_Search_Tree(Tree):
    def __init__(self):
        super().__init__()
    def contains(self,root,value):
        if root is None:
            return False

        if value == root.value:
            return True
        elif value < root.value:
            return self.contains(root.left, value)
        else:
            return self.contains(root.right, value)
    """
        Adds a new node with the given value to the binary search tree.

        If the tree is empty (root is None), the new node becomes the root.
        Otherwise, the method traverses the tree recursively to find the appropriate
        position to insert the new value based on the binary search tree property.

        Args:
            root: The root node of the tree (or subtree).
            value: The value to be inserted into the binary search tree.

    """
    def add_binary_search(self,root, value):
        if self.root is None:
            self.root = Node(value)
            
        else:
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    self.add_binary_search(root.left,value)
                
            elif value > root.value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    self.add_binary_search(root.right,value)
        

if __name__ == "__main__":
    # node1 = Node("A")
    # node1.left = Node("B")
    # node1.right = Node("C")
    # node1.left.left = Node("D")
    # node1.left.right = Node("E")
    # node1.right.left = Node("k")
    # node1.right.right = Node("g")
    # tree = Tree()
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
    print(tree1.find_maximum_value())

    # # binry = Binary_Search_Tree()
    # print(tree.pre_order(node1,list=[]))
    # tree.pre_order(tree.root,list=[])
    # print(tree.in_order(node1))
    # print(tree.post_order(node1))
    # # binry.add_binary_search(node1)
    bst = Binary_Search_Tree()
    bst.add_binary_search(bst.root,5)
    bst.add_binary_search(bst.root,3)
    bst.add_binary_search(bst.root,7)
    bst.add_binary_search(bst.root,2)
    bst.add_binary_search(bst.root,4)
    print(bst.find_maximum_value())

    # print(bst.pre_order(bst.root))
    # print(bst.contains(bst.root,9))



