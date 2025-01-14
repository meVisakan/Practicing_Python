# Move all the zeroes of a list to the end or to the start

def move_zero_end(my_list):
    non_zeros = [x for x in my_list if x != 0]
    zeros = [y for y in my_list if y == 0]
    print(non_zeros + zeros)


def move_zero_start(my_list):
    i = 0
    while i < len(my_list):
        if my_list[i] == 0:
            my_list.pop(i)
            my_list.insert(0, 0)
        else:
            i += 1
    print(my_list)


# Input
my_list = list(map(int, input("Enter the elements of the list with space separation: ").split()))
move_zero_end(my_list)
move_zero_start(my_list)
