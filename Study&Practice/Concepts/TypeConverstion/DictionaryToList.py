# Key value pairs of dictionary joined in a single list in the right order
def dict_list():
    my_dict = {"a": 1, "b": 2, "c": 3}

    # Key value pairs of dictionary joined in a single list in the right order
    all_ele = [x+y for x, y in zip(list(my_dict.keys()), list(map(str, (my_dict.values()))))]
    print(all_ele)

    # Keys and corresponding values in a single list but different elements
    flat_list = []
    for key, value in my_dict.items():
        flat_list.append(key)
        flat_list.append(value)
    print(flat_list)

    # Achieve the above using list comprehension
    flat_list2 = [item for pair in my_dict.items() for item in pair]
    print(flat_list2)

    # Keys separately in a list and values separately in the same list
    key_value = list(my_dict) + list(my_dict.values())
    print(key_value)


dict_list()

