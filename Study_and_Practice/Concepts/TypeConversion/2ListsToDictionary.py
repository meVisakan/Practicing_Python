# Merge two lists into a single dictionary

def list_dict(ls1, ls2):
    my_dict = dict(zip(ls1, ls2))
    print("\nNewly created dictionary:\n", my_dict)


# Input
ls1 = list(map(str, input("Enter the names with space separation: ").split()))      # a b c d e
ls2 = list(map(int, input("Enter the ages with space separation: ").split()))       # 10 21 8 68 11
list_dict(ls1, ls2)
