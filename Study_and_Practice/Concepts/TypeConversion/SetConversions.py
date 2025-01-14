# Write programs to convert a Set into a list, a tuple, a string and a dictionary

def set_conversion():
    # Set to List
    my_set = {1, 2, 3}
    my_list = list(my_set)
    print(my_list)

    # Set to Tuple
    my_set2 = {1, 2, 3, 4}
    my_tuple = tuple(my_set2)
    print(my_tuple)

    # Set to String
    my_set3 = {'1', 'b', '3', 'd'}
    my_str = "".join(my_set3)
    print(my_str)

    # Set to Dictionary
    my_set4 = {"a", 1, "b", 2}
    my_list4 = list(my_set4)    # Direct conversion from set to dict is not possible as set is not iterable
    my_dict = {my_list4[i]: my_list4[i+1] for i in range(0, len(my_list4), 2)}
    print(my_dict)


set_conversion()
