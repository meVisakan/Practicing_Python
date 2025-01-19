import random


# gives a random float number between 0 and 1
num1 = random.random()
print(f"Randomly generated number1: {num1}")


# gives a random float number in specified range
num2 = random.uniform(1, 100)
print(f"Randomly generated number2: {num2}")


# gives a random integer number in specified range
num3 = random.randint(1, 100)
print(f"Randomly generated number3: {num3}")


# gives a random number in a range with incremental steps
num4 = random.randrange(1, 100, 3)
print(f"Randomly generated number4: {num4}")


# gives a series of random numbers
num_list = random.sample(range(1, 100), 6)
print(f"Randomly generated number list: {num_list}")

