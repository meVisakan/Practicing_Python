# 5! = 5 * 4 * 3 * 2 * 1
# n! = n * n-1 * n-2 * ... * 1

def find_factorial(num):
    factorial = 1
    if num == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, num+1):
            factorial *= i
        print("Factorial of {} is {}".format(num, factorial))


# Input the number to find its factorial
number = int(input("Enter the number to find its factorial: "))
find_factorial(number)
