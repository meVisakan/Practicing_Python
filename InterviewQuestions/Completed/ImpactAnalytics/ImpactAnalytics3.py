nums = [19, 53, 2, 13, 37, 1, 13]


def sort_list(nums):
    l = len(nums)

    for i in range(l):
        for j in range(i+1, l):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    print(nums)


def remove_duplicate(nums):
    ndict = {}

    for i in nums:
        if i in ndict:
            ndict[i] += 1
        else:
            ndict[i] = 1

    originals = []
    for key, val in ndict.items():
        if val == 1:
            originals.append(key)

    print(originals)

sort_list(nums)
remove_duplicate(nums)
