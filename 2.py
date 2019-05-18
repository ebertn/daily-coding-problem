# Given an array of integers, return a new 
#   array such that each element at index i 
#   of the new array is the product of all 
#   the numbers in the original array except 
#   the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
#   the expected output would be 
#   [120, 60, 40, 30, 24]. If our input was 
#   [3, 2, 1], the expected output would be 
#   [2, 3, 6].

# Follow-up: what if you can't use division?

def withDivision(arr):
    total_prod = 1
    for num in arr:
        total_prod *= num

    return [total_prod // num for num in arr]
# O(n) time 
# O(n) memory

val = withDivision([1, 2, 3, 4, 5])
print(val)

def brute_force(arr):
    new_arr = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                new_arr[i] *= arr[j]

    return new_arr

# Looked up solution for division:
def withoutdivision(arr):
    l = len(arr)
    left = [1 for _ in range(l)]
    right = [1 for _ in range(l)]
    prod = [1 for _ in range(l)]

    for i in range(1,l):
        left[i] = arr[i-1] * left[i-1]

    for i in range(l-2, -1, -1):
        right[i] = arr[i+1] * right[i+1]

    for i in range(l):
        prod[i] = left[i] * right[i]

    return prod