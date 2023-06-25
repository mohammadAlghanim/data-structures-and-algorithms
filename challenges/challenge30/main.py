from HashTable import HashTable

hash_table = HashTable()

# Set key-value pairs
hash_table.set('name', 'John')
hash_table.set('age', 25)
hash_table.set('city', 'New York')


# Get values by key
print(hash_table.get('name'))
print(hash_table.get('age'))
print(hash_table.get('city'))

# Check if a key exists
print(hash_table.has('name'))
print(hash_table.has('email'))


# Get all keys
print(hash_table.keys())


# Calculate hash index for a key
print(hash_table.hash('name'))

