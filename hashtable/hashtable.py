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
            hash = hash ^ ord(char) # ord() will convert our string to the binary equivalent ascii number
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
        # See if the key value pair even exists
        index = self.hash_index(key)    # Get the index
        if self.storage[index] is None: # Edge case(?): If there is nothing at the index
            print("WARNING: Key not found") # Print the warning
            return                          # End the function
        if self.storage[index].key == key:  # If the key we're looking for is the first one at the index
            if self.storage[index].next is not None:    # If there is a next node
                self.storage[index] = self.storage[index].next  # Replace it with the next node to "delete" it
            else:                                       # If there isn't a next node
                self.storage[index] = None              # Set the first node at the index to None
        else:                                           # If the first key at the index pos is not the one we're looking for
            current = self.storage[index].next          # Start the cursor at the next one, because we already checked the first one above
            prev = self.storage[index]                  # Store the previous node
            while current is not None:                  # While current exists
                if current.key == key:                  # If the current node is the one we're looking for
                    prev.next = current.next            # Set the next of the previous to the node after the current, effectively deleting it
                    self.size -= 1                      # Decrement the size
                else:                             # If we didn't find the node we were looking for
                    prev = current                # Move previous to the current one
                    current = current.next        # Move current to the next one



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)    # Find out what index the key would be at 
        if self.storage[index] is None: # Edge case: See if there is anything at the index. If there isn't anything:
            return None                 # Return none
        current = self.storage[index]   # Create a pointer/cursor starting at the first node at the index
        while current:               # as long as there is something at the current node
            if current.key == key:      # If the node we're at has the key we're looking for
                return current.value    # Return the value
            else:                       # If it's not what we're looking for
                current = current.next  # Set current to the next node
        return None                     # if the while loop never returns something, then the node does not exist in the hashtable and we return None



    def resize(self, new_capacity): # Use if we filled up all of our indexes and need new ones
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity    # Update the capacity attribute to the new_capacity that was passed in
        old_storage = self.storage      # We're about to rewrite selfstorage, so we need to save it somewhere. No need to touch self.size
        self.storage = [None] * self.capacity # Rewrite storage to be a list of None's as long as self.capacity (which has been rewritten in line 185 to be new_capacity)
        for node in old_storage:        # Iterate through every node in the old storage
            if node is not None:        # If something exists at the index in old_storage
                self.put(node.key, node.value)  # Use the put method we created earlier to enter the nodes from the old_storage into the new_storage. The put method generates the index the key would be at and then adds the nodes where they need to go. We only need to move the head nodes of the linked lists, because the head nodes have the next attribute that will point to the rest of the linked list.



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
