# Write a function to implement bubble sort algorithm on a list

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print("Sorted array: ", arr)


arr = list(map(int, input("Enter the elements of the array with space separation: ").split()))
print("Input array: ", arr)
bubble_sort(arr)
