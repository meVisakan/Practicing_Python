#  A generator in Python returns an iterator that produces sequences of values one at a time.

def count_upto(n):
    num = 1
    while num <= n:
        yield num  # this makes our function a generator
        num += 1


# Using the generator
for number in count_upto(10):
    print(number)
