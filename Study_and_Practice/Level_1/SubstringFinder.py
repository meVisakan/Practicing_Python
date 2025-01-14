# Check whether a given substring is present in the given string or not

def substring_finder(s, sub_s):
    if s.find(sub_s) != -1:
        print("Substring is present in the given string")
    else:
        print("Substring is not present in the given string")


s = str(input("Enter a string: "))
sub_s = str(input("Enter the substring to be checked: "))
substring_finder(s, sub_s)
