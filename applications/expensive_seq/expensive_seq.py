# Your code here

lookup_table = {}   # Make a dictionary/hashtable
def expensive_seq(x, y, z):
    key = (x, y, z) # Store the tuple of x, y, and z into a variable called key because we use it so much
    if key not in lookup_table: # if the key is not in the lookup table, run the math below
        if x <= 0: 
            lookup_table[key] = y + z   # Once we get the result, store it into the lookup table
        if x >  0: 
            lookup_table[key] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)    # Once we get the result, store it into the lookup table
    return lookup_table[key] # Return the value of key
        



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
