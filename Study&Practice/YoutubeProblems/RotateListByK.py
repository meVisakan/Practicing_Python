# Rotate a list to the right by k places, where k is non-negative.

def rotate(nums, k):
    n = len(nums)

    if n == 0 or n == 1:
        print(nums)

    # Normalise k to avoid unnecessary full rotations
    k %= n
    rotated_nums = nums[-k:] + nums[:-k]

    print(rotated_nums)


# Input
nums = list(map(int, input("Enter the elements with space separation: ").split()))
k = int(input("Enter the number of rotations: "))
rotate(nums, k)
