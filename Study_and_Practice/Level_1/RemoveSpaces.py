# Remove all the spaces from the given string

def remove_space(s):
    result = ""
    for i in s:
        if i != " ":
            result += i
    print(result)


# Input
s = str(input("Enter a string: "))
remove_space(s)
