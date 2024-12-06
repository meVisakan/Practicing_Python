# Find all the substring of a string with length minimum k

def sub_strings(str1, k):
    n = len(str1)
    result = []
    for i in range(n):
        for j in range(i+1, n+1):
            sub = str1[i:j]
            if len(sub) >= k:
                result.append(sub)

    return result


# Input
str1 = str(input("Enter a string: "))
k = int(input("Enter the min substring length: "))
print(sub_strings(str1, k))
