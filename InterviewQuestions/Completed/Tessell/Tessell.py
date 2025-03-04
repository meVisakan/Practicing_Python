def sort_list(nums):
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    print(nums)


# Input
nums = [12, 31, 22, 44]
sort_list(nums)
