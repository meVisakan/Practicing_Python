# Rotate a string to the left by k places, where k is non-negative.

def rotate(chars, k):
    n = len(chars)

    if n == 0 or n == 1:
        print(chars)

    # Normalise k to avoid unnecessary full rotations
    k %= n
    rotated_chars = chars[k:] + chars[:k]

    print(rotated_chars)


# Input
chars = str(input("Enter the string: "))
k = int(input("Enter the number of rotations: "))
rotate(chars, k)
