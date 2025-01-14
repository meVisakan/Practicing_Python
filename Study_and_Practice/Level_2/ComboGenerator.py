# Given an integer n and an integer K, output a list of all the combination of k numbers chosen from 1 to n.

from itertools import combinations


def combo_gen(n, k):
    numbers = range(1, n+1)
    combos = list(combinations(numbers, k))
    print(combos)


# Input
n = int(input("Enter the range of elements: "))
k = int(input("Enter the number of elements in each combo: "))
combo_gen(n, k)
