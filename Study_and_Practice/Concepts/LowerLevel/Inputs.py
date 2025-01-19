# Write a program to fetch inputs for a list, set, tuple, string and dictionary from a user

def inputs():
    # List input
    my_list = list(input("Enter the elements with space separation for list: ").split())
    print(my_list)

    # Set input
    my_set = set(input("Enter the elements with space separation for set: ").split())
    print(my_set)

    # Tuple input
    my_tuple = tuple(input("Enter the elements with space separation for tuple: ").split())
    print(my_tuple)

    # String input
    my_str = input("Enter the string: ")
    print(my_str)

    # Dictionary input
    my_dict = {}
    n = int(input("Enter the number of elements in the dictionary: "))

    for i in range(n):
        key, value = input(f"Enter key value pair for {i+1} pairings (in the format- key:value): ").split(":")
        my_dict[key] = value
    print(my_dict)


inputs()
