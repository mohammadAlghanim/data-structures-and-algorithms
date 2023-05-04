import pytest
from stack_and_queue.Stack import Stack
from stack_and_queue.Queue import Queue
# challenges/stack_and_queue/Queue.py
def test_queue1():
    queue = Queue()
    expected = "Empty Queue"
    actual = str(queue)
    assert expected == actual
def test_queue2():
    queue=Queue()
    queue.enqueue("B")
    queue.enqueue("K")
    queue.enqueue("A")
    expected = "B -->K -->A --> None"
    actual = str(queue)
    assert expected == actual
def test_queue3():
    queue=Queue()
    queue.enqueue("B")
    queue.enqueue("K")
    queue.enqueue("A")
    assert queue.peek() == "B"
    assert queue.dequeue() == "B"
    assert queue.peek() == "K"
def test_queue4():
    queue=Queue()
    with pytest.raises(Exception):
     queue.enqueue("B")
     queue.enqueue("K")
     queue.enqueue("A")
     queue.dequeue()
     queue.dequeue()
     queue.dequeue()
     queue.dequeue()
def test_queue5():
    queue=Queue()
    with pytest.raises(Exception):
     queue.enqueue("B")
     queue.enqueue("K")
     queue.enqueue("A")
     queue.dequeue()
     queue.dequeue()
     queue.dequeue()
     queue.peek() 
    

    
    
def test_stack1():
    stack = Stack()
    expected = "Empty Stack"
    actual = str(stack)
    assert expected == actual
def test_stack2():
    stack=Stack()
    stack.push("B")
    stack.push("K")
    stack.push("A")
    expected = "A -->K -->B --> None"
    actual = str(stack)
    assert expected == actual
def test_stack3():
    stack=Stack()
    stack.push("B")
    stack.push("K")
    stack.push("A")
    assert stack.peek() == "A"
    assert stack.pop() == "A"
    assert stack.peek() == "K"
def test_stack4():
    stack=Stack()
    with pytest.raises(Exception):
     stack.push("B")
     stack.push("K")
     stack.push("A")
     stack.pop()
     stack.pop()
     stack.pop()
     stack.pop()
def test_stack4():
    stack=Stack()
    with pytest.raises(Exception):
     stack.push("B")
     stack.push("K")
     stack.push("A")
     stack.pop()
     stack.pop()
     stack.pop()
     stack.peek()
    

    

