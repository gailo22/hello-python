def square(x):
    return x * x

def make_add(x):
    def f(y):
        return x + y
    return f

def make_add_lambda(x):
    return lambda y: x + y