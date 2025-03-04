my_list = [3, 8, 2, 7, 4, 7, 8]
nums_dict = {}

for i in my_list:
    if i in nums_dict:
        nums_dict[i] += 1
    else:
        nums_dict[i] = 1

for key, val in nums_dict.items():
    print(f"{key} = {val}")
