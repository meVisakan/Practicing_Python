# Find the common elements among 3 lists

from collections import Counter


def common_three(ls1, ls2, ls3):
    # Using sets
    result1 = list(set(ls1).intersection(set(ls2)).intersection(set(ls3)))
    print(result1)

    # Using list comprehension
    result2 = [i for i in ls1 if i in ls2 and i in ls3]
    print(result2)

    # Using Counter
    # Create counters for each list
    c1 = Counter(ls1)
    c2 = Counter(ls2)
    c3 = Counter(ls3)

    common_counter = c1 & c2 & c3
    result3 = list(common_counter.elements())
    print(result3)


# Input
ls1 = list(map(int, input("Enter the elements of list1 with space separation: ").split()))
ls2 = list(map(int, input("Enter the elements of list2 with space separation: ").split()))
ls3 = list(map(int, input("Enter the elements of list3 with space separation: ").split()))
common_three(ls1, ls2, ls3)
