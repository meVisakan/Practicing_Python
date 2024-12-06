# Swap the first and last elements of an array

def swap_elements(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    print("Array after the elements swap: ", arr)

# Input
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
print(arr)
swap_elements(arr)

