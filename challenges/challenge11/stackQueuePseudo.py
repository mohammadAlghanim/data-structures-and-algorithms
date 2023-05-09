from challenges.stack_and_queue.Stack import Stack

class Pseudo_queue:
    """
     class named Pseudo_queue that implements a queue using two stacks.
    The class has two static variables, inbox and outbox, which are instances of the Stack class.
    The enqueue() method adds a value to the inbox stack. The dequeue() method removes and returns the first item from the queue by transferring items from the inbox stack to the outbox stack if the outbox is empty,
    then popping from the outbox stack. If both stacks are empty, it returns "Queue is empty".
    """
    def __init__(self) :
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self,value):
        self.inbox.push(value)
    def dequeue(self):
        if self.inbox.is_empty() and self.outbox.is_empty():
            return "Queue is empty"
        if self.outbox.is_empty() and not self.inbox.is_empty():
            size= self.inbox.get_size()
            for i in range(size):
                self.outbox.push(self.inbox.pop())
            return self.outbox.pop()
        if not self.outbox.is_empty():
            return self.outbox.pop()


ll = Pseudo_queue()
ll.enqueue(1)
ll.enqueue(2)
ll.enqueue(3)
print(ll.dequeue())
ll.enqueue(4)
print(ll.dequeue())


    
   