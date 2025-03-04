# Q - Print the largest three numbers from a number array


def largest_three(arr):
    l = len(arr)
    for i in range(l):
        for j in range(i+1, l):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr[:3])


# Input
arr = [5, -1, 3, 99, 4]
largest_three(arr)
