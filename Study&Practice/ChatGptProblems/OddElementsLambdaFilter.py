# Filter out the odd numbers from the list using lambda and filter

num_list = [1, 4, 6, 5]
odd_num = list(filter(lambda x: x % 2 != 0, num_list))
print(odd_num)
