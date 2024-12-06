# Find the 2nd largest element in the list

def second_largest(arr):
    if len(arr) < 2:
        print("List has less than 2 elements")
    unique_arr = list(set(arr))
    unique_arr.sort()
    print("Second largest element is: ", unique_arr[-2])


# Input array
arr = list(map(int, input("Enter the elements of the list with space separated: ").split()))
print(arr)
second_largest(arr)
