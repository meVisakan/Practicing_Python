# # Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
# # A pair (i, j) is fair if: 0 <= i < j < n, and lower <= nums[i] + nums[j] <= upper
# # Ex 1: nums = [0,1,7,4,4,5], lower = 3, upper = 6 Output: 6
#
# def valid_pairs(nums, lower, upper):
#     count = 0
#     # nums.sort()
#     # print(nums)
#     result = set()
#     for i in range(len(nums)):
#         for j in range(len(nums[1::])):
#             if (i < j) and lower <= nums[i] + nums[j] <= upper:
#                 result.add((i, j))
#                 # count += 1
#
#     print(len(result))
#     print(result)
#
#
# # Input
# nums = [0,1,7,4,4,5]
# lower = 3
# upper = 6
# valid_pairs(nums, lower, upper)
#
#
# Ex 2: nums = [1, 7, 9, 2, 5], lower = 11, upper = 11 Output = 1
# Explanation: (0, 3), (0, 4), (0, 5), (1, 3), (1, 4), and (1, 5)
#
# def valid_pairs(nums, lower,
#                 upper):    count = 0  # nums.sort()    # print(nums)    result = set()    for i in range(len(nums)):        for j in range(len(nums[1::])):            if (i < j) and lower <= nums[i] + nums[j] <= upper:                result.add((i, j))                # count += 1    print(len(result))    print(result)# Inputnums = [0,1,7,4,4,5]lower = 3upper = 6valid_pairs(nums, lower, upper)
