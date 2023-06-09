import pytest
from repeated_word import first_repeated_word
# #################### test first_repeated_word Function #################### #

def test_first_repeated_word():
    assert first_repeated_word('HELLO WORLD WORLD HELLO')=='WORLD'
    assert first_repeated_word('WORLD HELLO')==None
    assert first_repeated_word('WORLD HELLO HELLO WORLD')=='HELLO'
    

def test_first_repeated_word_2():
    assert first_repeated_word('WORLD HELLO')==None

def test_first_repeated_word_3():
    assert first_repeated_word('WORLD HELLO HELLO WORLD')=='HELLO'

def test_first_repeated_word_4():
    assert first_repeated_word('No Repetition :p')==None
    
    