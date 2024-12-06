# Program to write a Pascal's Triangle

from math import factorial


def pascal_triangle(n):
    for x in range(n):
        for y in range(n-x+1):
            print(end=" ")
        for y in range(x+1):
            # Formula for nCr = n!/r! * (n-r)!
            print(factorial(x)//(factorial(y) * factorial(x-y)), end=" ")
        print()


n = int(input("Enter the number of rows for the triangle: "))
pascal_triangle(n)
