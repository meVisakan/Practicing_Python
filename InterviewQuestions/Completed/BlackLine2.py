# Q - Rotate a list by k rotations

def rotate_list(q_list, k):
    n = len(q_list) // k

    r_list = q_list[n+1::] + q_list[n::]
    print("Original list: ", q_list)
    print("Rotated list: ", r_list)


# Input
q_list = list(map(int, input("Enter the elements of the list with comma separation: ").split(",")))
k = int(input("Enter the number of rotations: "))
rotate_list(q_list, k)

