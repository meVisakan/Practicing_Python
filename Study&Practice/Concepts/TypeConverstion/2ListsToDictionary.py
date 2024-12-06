# Merge two lists into a single dictionary

def list_dict(ls1, ls2):
    my_dict = dict(zip(ls1, ls2))
    print(my_dict)


# Input
ls1 = list(map(str, input("Enter the names with space separation: ").split()))
ls2 = list(map(int, input("Enter the ages with space separation: ").split()))
list_dict(ls1, ls2)
