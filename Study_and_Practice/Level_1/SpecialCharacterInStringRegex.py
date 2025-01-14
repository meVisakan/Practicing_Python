import re


def has_special_char(s):
    pattern = re.compile('[^a-zA-Z0-9 ]')
    if pattern.search(s):
        return True
    return False


s = str(input("Enter the string: "))
if has_special_char(s):
    print("Has special character")
else:
    print("Doesn't have special character")
