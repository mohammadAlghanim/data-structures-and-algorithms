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
    def pre_order(self, root,list =[]):
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
    def in_order(self,root,list =[]):
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
    def post_order(self,root,list=[]):

        if root is not None:
            # print(root.value)
            self.post_order(root.left,list)
            self.post_order(root.right,list)
            list.append(root.value)
        return list





# node1 = Node("A")
# node1.left = Node("B")
# node1.right = Node("C")
# node1.left.left = Node("D")
# node1.left.right = Node("E")
# node1.right.left = Node("k")
# node1.right.right = Node("g")
# tree = Tree()
# print(tree.pre_order(node1))
# # tree.pre_order(tree.root)
# print(tree.in_order(node1))
# print(tree.post_order(node1))
#############################################
class Binary_Search_Tree(Tree):
    def __init__(self):
        super().__init__()
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
        


node1 = Node("A")
node1.left = Node("B")
node1.right = Node("C")
node1.left.left = Node("D")
node1.left.right = Node("E")
node1.right.left = Node("k")
node1.right.right = Node("g")
tree = Tree()
# # binry = Binary_Search_Tree()
print(tree.pre_order(node1,list=[]))
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
print(bst.pre_order(bst.root,list= []))



