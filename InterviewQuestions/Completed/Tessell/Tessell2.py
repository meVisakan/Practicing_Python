# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1: Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2: Input: nums = [3,2,4], target = 6 Output: [1,2]
# Example 3: Input: nums = [3,3], targ Bhupendra Yadav 4:18 PM target = 6 Output: [0,1]

nums = [3, 2, 7, 11, 15]
target = 9


def sum_indexes(nums, target):
    present = {}
    for i, num in enumerate(nums):
        print(f"{i} = {num}")
        compliment = target - num
        if compliment in present:
            return present[compliment], i
        present[num] = i


print(sum_indexes(nums, target))
