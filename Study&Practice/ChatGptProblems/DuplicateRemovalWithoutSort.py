# Remove duplicates from the list without sorting and preserve the original order of elements.

def duplicate_order_removal(nums):
    if len(nums) < 1:
        print("Enter a proper list!")
    else:
        temp = []
        for i in nums:
            if i not in temp:
                temp.append(i)
            else:
                print(f"Duplicate is present for {i}")
        print(temp)


# Input
nums = list(map(int, input("Enter the elements of  the list with space separation: ").split()))
duplicate_order_removal(nums)
