# Find the sum of elements in an array

def sum_elements(array):
    summ = 0
    for i in array:
        summ += i
    print(f"Sum of all the elements in an array is: {summ}")


# Input the array
array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print(array)
sum_elements(array)
