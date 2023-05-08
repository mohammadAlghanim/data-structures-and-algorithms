
class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
class Stack:
    """
    This code defines a class called Stack that implements a basic stack data structure using a linked list. Here's an overview of its functionality:

    The Stack class has an initializer (__init__) that sets the top of the stack to None and the size to 0.

    The push method adds an element to the top of the stack. It creates a new node with the given value and makes it the new top. If the stack is not empty, the new node's next pointer is set to the previous top. The size of the stack is incremented by 1.

    The __str__ method is overridden to provide a string representation of the stack. It traverses the linked list from the top to the bottom and creates a string with the values of each node, separated by arrows (-->). If the stack is empty (top is None), it returns the string "Empty Stack".

    The pop method removes and returns the element at the top of the stack. It raises an exception if the stack is empty. The top is updated to the next node, and the size of the stack is decremented by 1.

    The peek method returns the value of the element at the top of the stack without removing it. It raises an exception if the stack is empty.

    The get_size method returns the current size of the stack.

    The is_empty method returns False if the stack is empty (size is 0), and True otherwise.

    In summary, this code provides the basic functionality of a stack data structure, allowing elements to be pushed onto the top of the stack, popped from the top, and peeked at without removal. The size and emptiness of the stack can also be determined.
    """
    def __init__(self) :
        self.top = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
            # self.top = node.next
        self.top= node
        self.size += 1
    def __str__(self):
        output = ""
        
        if self.top is None:
            return "Empty Stack"
        else:
            current = self.top
            while(current):
                output += f'{current.value} -->'
                current = current.next
            
            output += " None"
        return output
        
    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -=1
            return temp.value
        else:
            raise Exception("Empty")
        
    def peek(self):
        if self.top:
            return self.top.value
        else:
           raise Exception("Empty")
        
    def get_size(self):
        return self.size
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False