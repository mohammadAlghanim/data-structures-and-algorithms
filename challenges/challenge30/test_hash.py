import pytest
from HashTable import HashTable

@pytest.fixture
def hash_table():
    return HashTable()

def test_set_key_value(hash_table):
    hash_table.set('name', 'John')
    assert hash_table.get('name') == 'John'

    hash_table.set('age', 25)
    assert hash_table.get('age') == 25

    hash_table.set('city', 'New York')
    assert hash_table.get('city') == 'New York'


def test_retrieve_value(hash_table):
    hash_table.set('name', 'John')
    assert hash_table.get('name') == 'John'

    hash_table.set('age', 25)
    assert hash_table.get('age') == 25

    hash_table.set('city', 'New York')
    assert hash_table.get('city') == 'New York'

    assert hash_table.get('name') == 'John'
    assert hash_table.get('age') == 25
    assert hash_table.get('city') == 'New York'
def test_retrieve_non_existing_key(hash_table):
    hash_table.set('name', 'John')
    hash_table.set('age', 25)
    hash_table.set('city', 'New York')

    assert hash_table.get('email') is None
    assert hash_table.get('address') is None
    assert hash_table.get('phone') is None
def test_get_all_unique_keys(hash_table):
    hash_table.set('name', 'John')
    hash_table.set('age', 25)
    hash_table.set('city', 'New York')

    keys = hash_table.keys()
    expected_keys = ['age', 'city', 'name']
    assert sorted(keys) == expected_keys

def test_handle_collision(hash_table):
    hash_table.set('name', 'John')
    hash_table.set('eman', 'Jane')

    assert hash_table.get('name') == 'John'
    assert hash_table.get('eman') == 'Jane'

def test_retrieve_value_from_collision_bucket(hash_table):
    hash_table.set('name', 'John')
    hash_table.set('eman', 'Jane')

    assert hash_table.get('name') == 'John'
    assert hash_table.get('eman') == 'Jane'

def test_hash_key_to_in_range_value(hash_table):
    key = 'test_key'
    hash_index = hash_table.hash(key)

    assert 0 <= hash_index < hash_table.size
