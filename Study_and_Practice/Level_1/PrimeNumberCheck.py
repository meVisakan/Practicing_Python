# A prime number has the below conditions:
# natural number > 1
# has only 2 factors - 1 and itself


def check_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# Input
n = int(input("Enter a positive integer to check whether its prime or not: "))
if n < 1:
    print("Invalid input")
elif n == 1:
    print("1 is neither prime nor composite.")
elif check_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
