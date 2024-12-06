# Check if 2 strings are anagrams.
# Two string s are anagrams if they contain the same characters in the same frequency but in a different order

def check_anagram(str1, str2):
    if len(str1) != len(str2):
        print("The string are not anagrams as they have unequal lengths")
    else:
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)
        if sorted_str1 == sorted_str2:
            print("Entered strings are anagrams")
        else:
            print("Strings are not anagrams")


# Input
str1 = str(input("Enter string 1: "))
str2 = str(input("Enter string 2: "))
check_anagram(str1, str2)
