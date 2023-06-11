def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        temp = x
        x, y = y, x+y
        yield temp


for fib in fibonacci(15):
    print(fib)