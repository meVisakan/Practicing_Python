# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in seen:
            print([seen[compliment], i])
        seen[num] = i


# Input
nums = list(map(int, input("Enter the numbers for the list with space separation: ").split()))
target = int(input("Enter the target number: "))
two_sum(nums, target)
