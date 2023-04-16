class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linklist2:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node


    def insert_before(self, value, new_value):
      new_node = Node(new_value)
      if self.head is None:
        self.head = new_node
      elif self.head.value == value:
        new_node.next = self.head
        self.head = new_node
      else:
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        if current.next is None:
            return
        new_node.next = current.next
        current.next = new_node


    def insert_after(self,value,new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        current = self.head
        while current is not None:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                
            current = current.next
