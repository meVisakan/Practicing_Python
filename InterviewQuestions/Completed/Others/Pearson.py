nums = [21, 32, 11, 42, 56]
l = len(nums)
for i in range(l):
    for j in range(i+1, l):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(nums)
