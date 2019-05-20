def slow(l):
    l.sort()
    
    for i in range(1, len(l)):
        if l[i] != l[i - 1] and l[i] != l[i - 1] + 1:
            return l[i]

    return None

# Time:  O(nlogn), same as sort()
# Space: O(n), same as sort()

def minimum(l):
    smallest = l[0]
    for item in l:
        if item < smallest:
            smallest = item
    return smallest

def maximum(l):
    largest = l[0]
    for item in l:
        if item > largest:
            largest = item
    return largest

def nonconstant_space(l):
    seen = set(l) # Time: O(n), Space: O(n)

    min = minimum(l) # O(n)
    max = maximum(l) # O(n)

    for i in range(min, max + 2):
        if i > 0 and i not in seen:
            return i

    return None

# Time: O(n)
# Space: O(n)

print(nonconstant_space([3, 4, -1, 1]))
print(nonconstant_space([1, 2, 0]))

# Doesn't work with duplicates (or if negatives
# aren't ordered), at least not in O(n) space
def no_duplicates(l):
    min = minimum(l)
    max = maximum(l)

    total_sum = sum(range(min, max+1))
    l_sum = sum(l)

    diff = total_sum - l_sum

    return diff if diff != 0 else max+1

# Use array to mark duplicates

print(no_duplicates([3, 4, -1, 1]))
print(no_duplicates([1, 2, 0]))

def optimal(l):
    pass