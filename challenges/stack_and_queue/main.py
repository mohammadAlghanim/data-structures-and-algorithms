from Queue import Queue
from Stack import Stack
if __name__ == "__main__":
 queue1 = Queue()
 queue1.enqueue(1)
 queue1.enqueue(2)
 queue1.enqueue(3)
 
 
 
 stack1 = Stack()
 stack1.push(1)
 stack1.push(3)
 stack1.push(4)
 try:
  print(queue1.dequeue())
  print(queue1)
  print(stack1)
  print(stack1.pop())
  print(stack1.pop())
  print(stack1.pop())
  print(stack1.pop())
  print(stack1)

  print(stack1.get_size())
 except IndexError as err:
  print(err)