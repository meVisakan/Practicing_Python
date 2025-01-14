# Find the duplicates of elements present in the list

def find_duplicates(lst):
    counts = {}
    duplicate = []

    for l in lst:
        if l in counts:
            counts[l] += 1
        else:
            counts[l] = 1

    for key, value in counts.items():
        if value > 1:
            duplicate.append(key)

    print(duplicate)


# Input
lst = list(map(int, input("Enter the elements in the list with space separation: ").split()))
find_duplicates(lst)
