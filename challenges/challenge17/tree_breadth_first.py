class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Tree_breadth_first:
        def __init__(self):
           self.root = None
           self.insertion_order = []
        def insert(self, value):
         """
        Inserts a new node with the given value into the tree.

         Args:
            value: The value to be inserted.
          """
         new_node = Node(value)
         self.insertion_order.append(value)  # Add value to the insertion order list

         if self.root is None:
             self.root = new_node
         else:
            queue = [self.root]

            while queue:
                node = queue.pop(0)
                if node.left is None:
                    node.left = new_node
                    break
                elif node.right is None:
                    node.right = new_node
                    break
                else:
                    queue.append(node.left)
                    queue.append(node.right)
        def breadth_first(self):
          if self.root is None:
            return []

          queue = [self.root]
          values = []

          while queue:
            node = queue.pop(0)
            values.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

          return values
tree1 = Tree_breadth_first()
tree1.insert(2)
tree1.insert(8)
tree1.insert(74)
tree1.insert(7)
tree1.insert(10)
tree1.insert(6)
tree1.insert(8)

# node4 = Node(12)
# tree1.root.left.left = node4

# node5 = Node(6)
# tree1.root.left.right = node5

# node6 = Node(15)
# tree1.root.right.left = node6
print(tree1.breadth_first())