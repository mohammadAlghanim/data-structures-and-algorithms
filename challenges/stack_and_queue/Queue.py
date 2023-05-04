
class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
class Queue:
    """
    This code defines a class called Queue that implements a basic queue data structure using a linked list. Here's a breakdown of the functionality:

    The Queue class has an initializer (__init__) that sets the front and rear of the queue to None.

    The __str__ method is overridden to provide a string representation of the queue. It traverses the linked list from the front to the rear and creates a string with the values of each node, separated by arrows (-->). If the queue is empty (front is None), it returns the string "Empty Queue".

    The enqueue method adds an element to the rear of the queue. It creates a new node with the given value and assigns it as the rear. If the queue is empty, both the front and rear are set to the new node.

    The dequeue method removes and returns the element at the front of the queue. It raises an exception if the queue is empty. If there is only one node in the queue, it sets the rear to None. Otherwise, it updates the front to the next node and severs the connection to the previous front node.

    The peek method returns the value of the element at the front of the queue without removing it. It raises an exception if the queue is empty.

    Overall, this code provides the basic functionality of a queue data structure, allowing elements to be added to the rear and removed from the front of the queue, while maintaining the order of insertion.
    """
    def __init__(self):
        self.front=None
        self.rear = None

    def __str__(self):
        output = ""
        
        if self.front is None:
            return "Empty Queue"
        else:
            current = self.front
            while(current):
                output += f'{current.value} -->'
                current = current.next
            
            output += " None"
        return output
    def enqueue(self,value):
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next =node 
            self.rear= node

    def dequeue(self):
        if self.front == None:
            raise Exception("Empty")
        if self.front == self.rear:
            self.rear = None
            # self.front = None
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.value
    def peek(self):
        if self.front == None:
            raise Exception("Empty")
            # return "empty"
        return self.front.value




