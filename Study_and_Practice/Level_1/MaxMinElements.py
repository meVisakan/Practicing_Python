# Find the maximum and minimum elements in an array

def max_min_elements(arr):
    # with sorting
    new_arr = sorted(arr)
    minn = new_arr[0]
    maxx = new_arr[-1]
    print(f"The maximum and minimum elements of the array are {maxx} and {minn} respectively")

    # without sorting
    minn, maxx == arr[0], arr[-1]
    for i in arr:
        if i < minn:
            minn = i
        if i > maxx:
            maxx = i
    print(f"The maximum and minimum elements of the array are {maxx} and {minn} respectively")


# Input for array
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print(arr)
max_min_elements(arr)
