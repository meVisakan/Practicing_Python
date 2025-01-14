# Check if special character(s) is present in a given string

def has_special_char(s):
    for char in s:
        if not char.isalnum() and char != " ":
            return True
    return False


s = str(input("Enter the string: "))
if has_special_char(s):
    print("Has special character")
else:
    print("Doesn't have special character")
