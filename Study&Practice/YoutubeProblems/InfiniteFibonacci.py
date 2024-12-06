# Generate an infinite Fibonacci series using yield

def infinite_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b+a


f = infinite_fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
