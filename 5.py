# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) 
#   and cdr(pair) returns the first and last 
#   element of that pair. For example, 
#   car(cons(3, 4)) returns 3, and 
#   cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair

# Implement car and cdr.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def return_args(a, b):
    return (a, b)

def car(pair):
    a, b = pair(return_args)
    return a

def cdr(pair):
    a, b = pair(return_args)
    return b

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))