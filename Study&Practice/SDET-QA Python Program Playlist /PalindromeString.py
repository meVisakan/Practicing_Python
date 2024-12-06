# Check if a string is palindrome or not

def palindrome(s):
    rev_s = s[::-1]
    if rev_s == s:
        print("String is palindrome")
    else:
        print("String is not a palindrome")


s = input("Enter a string: ")
print(s)
palindrome(s)
