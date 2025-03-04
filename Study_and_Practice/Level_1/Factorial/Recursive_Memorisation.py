# Finding the factorial of a number using memorization

memo = {0: 1}


def factorial_memory(num):
    if num in memo:
        return memo[num]
    memo[num] = num * factorial_memory(num-1)
    return memo[num]


# Input the number and find its factorial
try:
    number = int(input("Enter the number: "))
    result = factorial_memory(number)
    print(f"Factorial of {number} is: {result}")
except ValueError:
    print("Please enter a valid integer.")
