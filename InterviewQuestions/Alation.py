# Merge two arrays after sorting them.


def merge_sort(arr1, arr2):
    merged_arr = arr1 + arr2
    merge_arr2 = sorted(merged_arr)
    print("Sorted, merged array: ", merge_arr2)


# Input
arr1 = list(map(int, input("Enter the elements of the array1 with space separation: ").split()))
arr2 = list(map(int, input("Enter the elements of the array2 with space separation: ").split()))
merge_sort(arr1, arr2)
