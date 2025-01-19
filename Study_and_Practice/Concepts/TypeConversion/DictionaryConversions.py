# Write programs to convert a Dictionary into a list, a set, a tuple and a string

def dict_conversion(my_dict):

    # Dictionary to List
    my_list_keys = list(my_dict)    # Only keys
    my_list_keys2 = list(my_dict.keys())    # Only keys, mentioned explicitly
    my_list_values = list(my_dict.values())   # Only values, mentioned explicitly
    print(my_list_keys)
    print(my_list_keys2)
    print(my_list_values)

    # Dictionary to Set
    my_set = set(my_dict)
    print(my_set)   # Only keys, in random order

    # Dictionary to Tuple
    my_tuple = tuple(my_dict)
    print(my_tuple)   # Only keys taken automatically

    # Dictionary to String
    my_str = "".join(my_dict)
    print(my_str)


# Input
my_dict = {"a": 1, "b": 2, "c": 3}
dict_conversion(my_dict)
