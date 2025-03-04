# 5! = 5 * 4 * 3 * 2 * 1
# n! = n * n-1 * n-2 * ... * 1

def find_factorial(num):
    factorial = 1
    if num < 0:
        return f"\nFactorial does not exist for {num} as it is a negative number."
    if num >= 1:
        for i in range(1, num+1):
            factorial *= i
    return f"\nFactorial of {num} is {factorial}."


# Input the number to find its factorial
number = int(input("Enter the number to find its factorial: "))
print(find_factorial(number))
