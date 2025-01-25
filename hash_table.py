class HashTable:
    def __init__(self, size=10):
       #Initialize the hash table with a given size. 
        self.size = size
        self.table = [[] for _ in range(size)]  # Each slot is a chain (list)

    def hash_function(self, key):
       #Hash function to calculate the index for a given key. 
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if the key exists; update the value if found
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key doesn't exist, append it to the chain
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        # Look for the key in the chain at the calculated index
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value if found
        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        # Look for the key in the chain and remove it
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True  # Key successfully deleted
        return False  # Key not found

if __name__ == "__main__":
    # Create a hash table
    hash_table = HashTable(size= 4)

    # Insert key-value pairs
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value3")
    hash_table.insert("key1", "updated_value1")  # Update key1's value

    # Search for keys
    print("\nSearch Results:")
    print("key1:", hash_table.search("key1"))  # Should return "updated_value1"
    print("key2:", hash_table.search("key2"))  # Should return "value2"
    print("key4:", hash_table.search("key4"))  # Should return None (not found)

    # Delete a key
    print("\nDeleting key2...")
    if hash_table.delete("key2"):
        print("key2 deleted.")
    else:
        print("key2 not found.")

    # Attempt to search for the deleted key
    print("key2 after deletion:", hash_table.search("key2"))  # Should return None
