import pytest
from challenges.challenge12.stack_queue_animal_shelter import AnimalShalter
def test_animal_cat(AA):
    assert AA.dequeue("cat") == {'species': 'cat', 'name': 'ddd'}
def test_animal_dog(AA):
    assert AA.dequeue("dog") == {'species': 'dog', 'name': 'fff'}

@pytest.fixture
def AA():
    AA = AnimalShalter()
    AA.enqueue({"species":"cat","name":"ddd"})
    AA.enqueue({"species":"dog","name":"fff"})
    AA.enqueue({"species":"cat","name":"kkk"})
    AA.enqueue({"species":"cat","name":"jjj"})

    return AA