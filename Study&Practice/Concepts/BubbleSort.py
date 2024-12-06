# Write a function to implement bubble sort algorithm on a list

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array: ", arr)


arr = list(map(int, input("Enter the elements of the array with space separation: ").split()))
print("Input array: ", arr)
bubble_sort(arr)
