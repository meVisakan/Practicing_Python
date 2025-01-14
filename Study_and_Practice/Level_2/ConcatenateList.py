# Concatenate the elements present in two lists individually as well as a whole

def concat_list(ls1, ls2):
    # concat = [x + y for x, y in zip(ls1, ls2)] ### for equal length
    concat = []
    if len(ls1) == len(ls2):
        for i in range(len(ls1)):
            concat.append(ls1[i]+ls2[i])
    else:
        if len(ls1) > len(ls2):
            diff = len(ls1) - len(ls2)
            print("Diff1: ", diff)
            for j in range(len(ls2)):
                concat.append(ls1[j] + ls2[j])
            for k in ls1[len(ls1) - diff::]:
                concat.append(k + "!")
        else:
            diff = len(ls2) - len(ls1)
            print("Diff2: ", diff)
            for l in range(len(ls1)):
                concat.append(ls1[l] + ls2[l])
            for m in ls2[len(ls2) - diff::]:
                concat.append(m + "!")
    print(concat)


# Input
ls1 = list(map(str, input("Enter the elements of the list 1 with space separation: ").split()))
ls2 = list(map(str, input("Enter the elements of the list 2 with space separation: ").split()))
concat_list(ls1, ls2)
