# Sort a list without using the sorting function

def sort_without_sort(arr):
    l = len(arr)
    maxx = arr[0]
    for i in range(l):
        if arr[i] > maxx:
            maxx = arr[i]
    print(maxx)


# Input
arr = list(map(int, input("Enter the elements of the list with space separation: ").split()))
sort_without_sort(arr)
