# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
# elements. Example 1: Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0] Example 2: Input: nums = [0] Output: [0]

def move_zeros(nums):
    l = len(nums)
    for i in range(l):
        if nums[i] == 0:
            nums.pop(i)
            print(nums)
            nums.insert(l-1, 0)
    print(nums)


# Input
nums = [0, 1, 0, 3, 12]
move_zeros(nums)
