# Remove duplicates from a list using sort() and without using set()

def rem_dup(my_list):
    my_list.sort()
    i = 0
    while i < (len(my_list) - 1):
        if my_list[i] == my_list[i+1]:
            my_list.pop(i+1)
        else:
            i += 1
    print(my_list)


# Input
my_list = list(map(int, input("Enter the elements in the list with space separation: ").split()))
rem_dup(my_list)
