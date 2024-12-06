# Find the factorial of a number with single line of code using Recursion


def factorial(num):
    return 1 if (num == 0 or num == 1) else num * factorial(num-1)


# Input
number = int(input("Enter the number to find its factorial: "))
print(factorial(number))
