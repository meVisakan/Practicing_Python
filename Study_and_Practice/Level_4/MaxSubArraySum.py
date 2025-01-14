# Given an array of integers, return the sum of the subarray with the largest sum.

# def max_subarray_sum(nums):
#     max_sum = current_sum = nums[0]
#     for num in nums[1:]:
#         # Compare the current number with the sum of the current subarray and decide whether
#         # to start a new subarray or continue the current one
#         current_sum = max(num, current_sum + num)
#         # Update max_sum if the current subarray sum is larger than the max_sum so far
#         max_sum = max(max_sum, current_sum)
#     print(max_sum)


def max_subarray_sum_array(nums):
    max_sum = current_sum = nums[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    print("Subarray with max sum: ", nums[start:end + 1])
    print("Maximum sum: ", max_sum)


# Input
nums = list(map(int, input("Enter the elements of the array with space separation: ").split()))
# max_subarray_sum(nums)
max_subarray_sum_array(nums)
