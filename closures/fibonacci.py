
def fibonacci():
    """
        closure is nested function defined inside other function
        it remembers variable defined in the outside function even \
        after the outside function call ends.
    """
    x, y = 0, 1
    def wrapper():
        nonlocal x,y
        temp = x
        x, y = y, x+y
        return temp
    return wrapper

fib = fibonacci()
for i in range(10):
    print(fib())