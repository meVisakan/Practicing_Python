# Write programs to convert a Tuple into a list, a set, a string and a dictionary

def tuple_conversion():
    # Tuple to List
    my_tuple = (1, 2, 3)
    my_list = list(my_tuple)
    print(my_list)

    # Tuple to Set
    my_tuple2 = (1, 1, 2, 3, 4)
    my_set = set(my_tuple2)
    print(my_set)

    # Tuple to String
    my_tuple3 = ('1', 'b', '3', 'd')
    my_str = "".join(my_tuple3)
    print(my_str)

    # Tuple to Dictionary
    my_tuple4 = ("a", 1, "b", 2)
    my_dict = {my_tuple4[i]: my_tuple4[i+1] for i in range(0, len(my_tuple4), 2)}
    print(my_dict)


tuple_conversion()
