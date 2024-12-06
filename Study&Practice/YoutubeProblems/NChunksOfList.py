# Break a list into n chunks of lists and add 0s at the end if no elements are left

def break_list(listt):
    out = [listt[i:i+n] for i in range(0, len(listt), n)]

    if len(out[-1]) < n:
        for _ in range(n-len(out[-1])):
            out[-1].append(0)

    print(out)


listt = list(input("Enter the list elements with space separated: ").split())
n = int(input("Enter the number of elements to be present in each sublist: "))
break_list(listt)
