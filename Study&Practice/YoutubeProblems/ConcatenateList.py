# Concatenate the elements present in two lists individually as well as a whole

def concatenate_lists(list1, list2):
    # con_list = [x + y for x, y in zip(list1, list2)]
    temp = ""
    con_list = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if i == j:
                temp = list1[i] + list2[j]
            else:
                pass
        con_list.append(temp)
    print(con_list)


list1 = list(map(str, input("Enter the elements of list1 with space separated: ").split()))
list2 = list(map(str, input("Enter the elements of list2 with space separated: ").split()))
concatenate_lists(list1, list2)
