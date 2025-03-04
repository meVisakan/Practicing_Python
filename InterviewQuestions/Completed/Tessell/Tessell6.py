# Q - Print star pattern like a Christmas tree

def star_pattern(n):
    for i in range(n):
        spaces = ' ' * (2*(n - i - 1))
        stars = '* ' * (2*i + 1)
        print(spaces + stars.strip())


# Input
n = 5
star_pattern(n)
