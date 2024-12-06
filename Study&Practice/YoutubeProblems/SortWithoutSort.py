# Sort a list without using the sorting function

def sort_without_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(i+1, n):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    print(l)


l = list(map(int, input("Enter the elements of the list with space separation: ").split()))
sort_without_sort(l)
