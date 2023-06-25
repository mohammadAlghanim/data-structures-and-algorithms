from LinkedList import LinkedList

class HashTable:
    def __init__(self, size=100):
        """
        Initialize the HashTable with a given size.

        Args:
            size (int): Size of the hash table.

        Returns:
            None
        """
        self.size = size
        self.map = [None] * size

    def set(self, key, value):
        """
        Set a key-value pair in the hash table, handling collisions as needed.

        Args:
            key: Key to be stored.
            value: Value associated with the key.

        Returns:
            None
        """

        index = self.hash(key)
        
        if self.map[index] is None:
            
            self.map[index] = LinkedList()
            self.map[index].add((key, value))
        else:
            
            node = self.map[index].head
            while node:
                if node.data[0] == key:
                    
                    node.data = (key, value)
                    return
                node = node.next

           
            self.map[index].add((key, value))

    def get(self, key):
       """
        Retrieve the value associated with a key from the hash table.

        Args:
            key: Key to retrieve the value.

        Returns:
            Value associated with the key.

        Raises:
            KeyError: If the key does not exist in the hash table.
        """
       index = self.hash(key)

       if self.map[index] is not None:
          node = self.map[index].head
          while node:
            if node.data[0] == key:
                return node.data[1]
            node = node.next

       return None  


    def has(self, key):
        """
        Check if a key exists in the hash table.

        Args:
            key: Key to check.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        index = self.hash(key)

        if self.map[index] is not None:
            node = self.map[index].head
            while node:
                if node.data[0] == key:
                    return True
                node = node.next

        return False

    def keys(self):
        """
        Return a collection of all unique keys in the hash table.

        Returns:
            list: Collection of keys.
        """
        keys = []

        for bucket in self.map:
            if bucket is not None:
                node = bucket.head
                while node:
                    keys.append(node.data[0])
                    node = node.next

        return keys

    def hash(self, key):
        """
        Hash the key to determine the index in the hash table.

        Args:
            key: Key to hash.

        Returns:
            int: Index in the hash table for the key.
        """
        return hash(key) % self.size
