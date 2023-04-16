import pytest
from link_list.challenge5.linklist.linked_list import Linklist
from link_list.challenge6.linklist.linked_list import Linklist

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



def test_6():
   ll=Linklist()
   ll.append("a")
   ll.append("b")
   excepted = 'a -->b --> None'
   actual = str(ll)
   assert actual == excepted
   


""" this test for the adding after """
def test_7():
   ll=Linklist()
   ll.append("a")
   ll.append("b")
   ll.insert_after("a","v")
   excepted = 'a -->v -->b --> None'
   actual = str(ll)
   assert actual == excepted
"""this test for the adding before"""
def test_8():
   ll=Linklist()
   ll.append("a")
   ll.append("b")
   ll.insert_before("a","v")
   excepted = 'v -->a -->b --> None'
   actual = str(ll)
   assert actual == excepted

   
  






@pytest.fixture
def ll():
    ll = Linklist()
    ll.insert("A")
    ll.insert("K")
    ll.insert("B")
    return ll