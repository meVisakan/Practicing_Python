# Write programs to convert a List into a set, a tuple, a string and a dictionary

def list_conversion():
    # List to Set
    my_list = [1, 2, 3, 3, 4]
    my_set = set(my_list)
    print(my_set)

    # List to Tuple
    my_list2 = [1, 2, 3, 4, 4]
    my_tuple = tuple(my_list2)
    print(my_tuple)

    # List to String
    my_list3 = ['1', 'b', '3', 'd']
    my_str = "".join(my_list3)
    print(my_str)

    # List to Dictionary
    my_list4 = ["a", 1, "b", 2]
    my_dict = {my_list4[i]: my_list4[i+1] for i in range(0, len(my_list4), 2)}
    print(my_dict)


list_conversion()
