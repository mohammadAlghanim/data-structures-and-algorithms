import pytest
from challenge11.stackQueuePseudo import Pseudo_queue

def test_PS_1 (AA):
    assert AA.dequeue() == 'A'

def test__PS_2():
    PQ = Pseudo_queue()
    assert PQ.dequeue() == "Queue is empty"

def test_PS_3(AA):
    
    assert str(AA.inbox) == "C -->B -->A --> None"

def test_PS_4(AA):
    AA.dequeue()
    assert str(AA.outbox) ==  "B -->C --> None" 

@pytest.fixture
def AA():
    AA = Pseudo_queue()
    AA.enqueue('A')
    AA.enqueue('B')
    AA.enqueue('C')
    return AA