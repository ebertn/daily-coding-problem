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