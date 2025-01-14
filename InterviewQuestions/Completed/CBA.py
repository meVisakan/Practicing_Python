# Q - Identify the common elements in 2 lists of numbers and print their total number of occurrence against them

def union_numbers(nums1, nums2):
    nums1.extend(nums2)

    union_dict = {}
    for i in nums1:
        if i in union_dict:
            union_dict[i] += 1
        else:
            union_dict[i] = 1

    result = {key: val for key, val in union_dict.items() if val > 1}

    print(result)


# Input
nums1 = [1, 2, 3, 5, 6]
nums2 = [2, 4, 5, 6]
union_numbers(nums1, nums2)
