my_list = [[10, 20, 30], [40, 50, 60], 66, [70, 80, 90], 100]

result2 = []
for i in my_list:
    if type(i) == list:
        result2.extend(i)
    else:
        result2.append(i)

print(result2)
