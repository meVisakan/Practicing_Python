# Rotate a string in either direction by n places, where n is non-negative.

def rotate(ls, direction, n):
    l = len(ls)

    if l == 0:
        print("Invalid Input!")
        return

    if l == 1 or n == 0:
        print(ls)
        return

    n %= l
    if direction.lower() == "right":
        print(ls[-n:] + ls[:-n])
    elif direction.lower() == "left":
        print(ls[n:] + ls[:n])
    else:
        print("Invalid Direction!")


# Input
try:
    ls = list(map(int, input("Enter the elements to be rotated in the string: ").split()))
    direction = str(input("Enter the direction of rotation: "))
    n = int(input("Enter the number of rotations: "))
    rotate(ls, direction, n)
except ValueError:
    print("Please provide the right input!!!")
