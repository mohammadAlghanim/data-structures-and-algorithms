import pytest
from challenges.challenge13.stack_queue_brackets import validate_brackets
def test_one():
    s = "()"
    actual= validate_brackets(s)
    expected =True
    assert actual == expected
def test_two():
    s = "(){"
    actual= validate_brackets(s)
    expected =False
    assert actual == expected
def test_three():
    s = "(){;jaij}"
    actual= validate_brackets(s)
    expected =True
    assert actual == expected
def test_four():
    s = ")[]"
    actual= validate_brackets(s)
    expected =False
    assert actual == expected