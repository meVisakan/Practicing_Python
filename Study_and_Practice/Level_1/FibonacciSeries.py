# Fibonacci series is

def fibonacci_series(num):
    a, b = 0, 1
    for _ in range(num):
        print(a, end=" ")
        a, b = b, b+a


# Input the number of terms to get the Fibonacci series
number = int(input("Enter the number of terms: "))
fibonacci_series(number)
