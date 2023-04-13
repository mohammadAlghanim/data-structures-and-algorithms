import pytest
from challenge5.linklist.linked_list import Linklist

def test_list1():
  ll = Linklist()
  expected = "Empty LinkeList"
  actual = str(ll)
  assert expected == actual

def test_list2(ll):
    expected = "B -->K -->A --> None"
    actual = str(ll)
    assert expected == actual

def test_list3():
   ll= Linklist()
   ll.insert("A")
   ll.insert("B")
   ll.insert("C")
   assert str(ll) == "C -->B -->A --> None"


def test_4(ll):
   a=ll.includes("A")
   q=ll.includes("Q")
   assert  q == False
   assert  a == True

def test_5(ll):
 assert  ll.head.value== "B"







@pytest.fixture
def ll():
    ll = Linklist()
    ll.insert("A")
    ll.insert("K")
    ll.insert("B")
    return ll