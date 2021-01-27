"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

cache = {}                      # Create outside so it 

def f(x):
    if x not in cache:          # If x is not in the cache
        cache[x] = x * 4 + 6    # Create a new entry in the cache

    return cache[x]             # return cache at x

# Your code here
# for a in q:
#     for b in q:
#         result = f(a) + f(b)
    #     for c in q:
    #         for d in q:
    #             if result == f(c) - f(d):
    #                 print(a, b, c, d)

