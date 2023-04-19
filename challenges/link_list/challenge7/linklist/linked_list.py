class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None
    
    count=0

    def insert(self,value):
        Linklist.count +=1
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next =self.head
            self.head =newNode

    def includes(self,key):
        temp= self.head
        while temp is not None:
            if temp.value == key:
                return True
            temp = temp.next
        if temp is None:
            return False
        
    def __str__(self):
        output = ""
        
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} -->'
                current = current.next
            
            output += " None"
        return output
    

    """This code adds a new node with the given value to the end of a linked list.

It creates a new node with the given value and sets it as the head if the linked
 list is empty, otherwise it iterates to the end of the list and sets the next
   reference of the last node to the new node."""
    def append(self, value):
        Linklist.count +=1
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    """This code inserts a new node with a given value before the first occurrence of a node with a given value in a linked list.

It creates a new node object with the given new_value and sets its next reference to None.
 If the list is empty, the new node becomes the head. Otherwise,
 it iterates through the list using two pointers and inserts the new node before the first occurrence of the node with the given value."""

    def insert_before(self, value, new_value):
       Linklist.count +=1
       node = Node(new_value)
       if self.head == None:
        self.head = node
       else:
         current = self.head
         previous = None
         while current:
            if current.value == value:
                node.next = current
                if previous:
                    previous.next = node
                else:
                    self.head = node
                return
            previous = current
            current = current.next


    
     
    """Create a new node with the given new_value and set its next reference to None.
Iterate through the linked list until the first occurrence of a node with the given value is found.
Insert the new node after the current node by adjusting the next references of the nodes involved"""

    def insert_after(self,value,new_value):
        Linklist.count +=1
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        current = self.head
        while current is not None:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                
            current = current.next
            
    def kthFromEnd(self,k):
        if self.head is None:
            return "Error : the linked list is empty"
        elif k >= Linklist.count:
            return "Error : Your input can't be more than the length"  
        elif k < 0 :
            return "Error : only positive numbers are accepted!"
        elif Linklist.count == 1:
            return self.head.value
        else:        
         pointer_one = self.head
         pointer_two = self.head

         for i in range(k):
            pointer_two = pointer_two.next

         while pointer_two.next is not None:
           pointer_one = pointer_one.next
           pointer_two = pointer_two.next

         return pointer_one.value
                
   



             
            