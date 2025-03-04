# Q - Sort the given string in asc order

def sort_string(s):
    ls = list(s)

    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]

    print(''.join(ls))


# Input
s = "andjfnlkdfn"
sort_string(s)
