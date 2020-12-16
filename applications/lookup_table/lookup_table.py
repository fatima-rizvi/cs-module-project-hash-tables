# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

lookup_table = {}   # Create a dictionary, which is a hashtable, that we'll use to lookup if we've already calculated these values. It has to be outside the function or it'll get rewritten everytime as a new dictionary
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # key = (x, y)    # The key will be a tuple of x and y. Making a key isn't necessary
    # if key in lookup_table:     # Find if the key is already in the lookup table. If you don't create a key, just pass in (x, y)(?)
    #     return lookup_table[key]    # If it is, return the value.  
    # # If it isn't: No need for an else statement bc of the return above
    # v = math.pow(x, y)          # Do the math from above
    # v = math.factorial(v)
    # v //= (x + y)
    # v %= 982451653
    # lookup_table[key] = v   # Add the new key and value pair into the dictionary
    # return lookup_table[key]    # You could also do "v"

    # Here's a way to do it without an else statement and without making a key
    if (x, y) not in lookup_table:  # If x and y in this order is not already in the lookup_table
        v = math.pow(x, y)          # Do the math from above
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        lookup_table[(x, y)] = v
    return lookup_table[(x, y)]     # Return the value of the tuple of (x, y) in the lookup table. If it was already in the table, the if statement won't run and this works just fine. If it wasn't in the table, we added it above in the if statement.



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
