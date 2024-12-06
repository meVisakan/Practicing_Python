# Find the maximum and minimum elements in an array

def max_min_elements(arr):
    maxx = arr[0]
    minn = arr[-1]
    for i in arr:
        if i > maxx:
            maxx = i

    for j in arr:
        if j < minn:
            minn = j

    print(f"The maximum and minimum elemnts of the array are {maxx} and {minn} respectively")


# Input for array
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print(arr)
max_min_elements(arr)
