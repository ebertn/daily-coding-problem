# Given a list of numbers and a number k, 
#     return whether any two numbers from 
#     the list add up to k.

# For example, given [10, 15, 3, 7] and 
#     k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?
def contains_sum(l, k):
    assert(k > 0)
    needed = set()
    for item in l:
        if item in needed:
            return True
        needed.add(k - item)

    return False
# O(n) time, assuming hashtable lookup is O(1)
# O(n) memory

print(contains_sum([10, 15, 3, 6], 17))