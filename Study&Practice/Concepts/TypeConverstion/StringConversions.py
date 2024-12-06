# Write programs to convert a String into a list, a set, a tuple and a dictionary

def string_conversion():
    # String to List
    my_str = "a2b4c6 abab"
    my_list = list(my_str)
    print(my_list)

    # String to Set
    my_str2 = "a2bb4cc"
    my_set = set(my_str2)
    print(my_set)

    # String to Tuple
    my_str3 = "aabbcc"
    my_tuple = tuple(my_str3)
    print(my_tuple)

    # String to Dictionary
    my_str4 = "a2b4c6d8"
    my_dict = {my_str4[i]: my_str4[i+1] for i in range(0, len(my_str4), 2)}
    print(my_dict)


string_conversion()
