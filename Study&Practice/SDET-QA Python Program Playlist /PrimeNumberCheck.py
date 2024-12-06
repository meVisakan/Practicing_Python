# A prime number has the below conditions:
# natural number > 1
# has only 2 factors - 1 and itself


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Input the number to be checked for prime
number = int(input("Enter the number to check for prime: "))
if is_prime(number):
    print("The number is prime")
else:
    print("The number is not prime")


