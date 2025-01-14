# Break a list into n chunks of lists and add 0s at the end if no elements are left

def break_list(ls, n):
    output = []
    for i in range(0, len(ls), n):
        output.append(ls[i:i+n])
    diff = n - len(output[-1])
    if diff > 0:
        output[-1].extend([0] * diff)
    print(output)


# Input
ls = list(map(int, input("Enter the elements of the list with space separation: ").split()))
n = int(input("Enter the number of elements in a chunk: "))
break_list(ls, n)
