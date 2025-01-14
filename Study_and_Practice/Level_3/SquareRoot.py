# Find the square root of a number

import cmath


def square_root(num):
    if type(num) == float:
        sqrt = num ** 0.5
    else:
        sqrt = cmath.sqrt(num)
    print(f"Square root of {num} is {sqrt}")


try:
    num = float(input("Enter a real number: "))
except ValueError:
    print("Entered number is not real.")
    num = complex(input("Enter the complex number: "))
square_root(num)
