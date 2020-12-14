class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

# The hashing function does the hashing bit. You input a string, it outputs a number
# A hash table using the hashing functin to take the key of a key value pair and hash it into an index

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity            # Potential size
        self.storage = [None] * capacity    # This will fill our list with a capacity number of None's
        self.size = 0                       # We'll start at zero and count them as we add them


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity    # self.capacity is the number of slots we passed in at the beginning. This is the potential size.


    def get_load_factor(self):
        """
        Return the load factor (asking how full this is) for this hash table.

        Implement this.
        """
        return (self.size / self.capacity) #Return the percentage/fraction/portion of how full this is
        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # algorithm fnv-1 :
        #     hash := FNV_offset_basis
        #     for each byte_of_data to be hashed do
        #         hash := hash × FNV_prime
        #         hash := hash XOR byte_of_data
            # return hash

        FNV_prime = 1099511628211
        FNV_offset = 14695981039346656037
        
        hash = FNV_offset
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char) # ord() will convert our srting to the binary equivalent ascii number
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)    # hash_index is a method
        node = HashTableEntry(key, value)   # hashTableEntry is a class
        if self.storage[index] is not None: # If there are nodes already at the index
            if self.storage[index].key == key:  #If the first item at the index is the one we're looking for
                self.storage[index].value = value # update the value. No need to increment the size because it already existed
            else:                                   # If the first item is not what we were looking for
                current = self.storage[index]       # Create a pointer/cursor variable that holds the current node we're looking at
                while current.next is not None:     # As long as there is a next value
                    if current.key == key:          # If the current node is the one we were looking for
                        current.value = value       # Then update the node's value
                    else:                           # If the current node is not the one we were looking for
                        current = current.next      # The move the pointer to the next node
                if current.key == key:          # This catches the edge case since our while loop will not hit the very last node. If the last node is the one we want
                    current.value = value       # Then update the value
                else:                           # If the key was not in the list
                    current.next = node         # Add the new node to the end
                    self.size += 1              # Increment self.size up by one


        else:                               # If there is nothing at the index
            self.storage[index] = node      # Add the node to self.storage at index
            self.size += 1                  # Increment self.size up by one
            

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
