# Given two strings text1 and text2, return the length of their longest common subsequence.
# If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

def long_com_sub(str1, str2, i, j):
    # If any string is empty, no common subsequence
    if i == len(str1) or j == len(str2):
        return 0
    # If characters match, move both pointers and increase count by 1
    if str1[i] == str2[j]:
        return 1 + long_com_sub(str1, str2, i+1, j+1)
    # If characters don't match, check both possibilities:
    # 1. Skip current character in text1
    # 2. Skip current character in text2
    return max(long_com_sub(str1, str2, i+1, j), long_com_sub(str1, str2, i, j+1))


def lcs_non_recursive(str1, str2):
    # Initialize variables
    i, j = 0, 0
    lcs_length = 0

    # Iterate through both strings
    while i < len(str1) and j < len(str2):
        # If characters match, increase the LCS length and move both pointers
        if str1[i] == str2[j]:
            lcs_length += 1
            j += 1  # Move pointer in str2
        # Always move the pointer in str1
        i += 1

    return lcs_length


# Input and function call
str1 = input("Enter string1: ")
str2 = input("Enter string2: ")
result1 = long_com_sub(str1, str2, 0, 0)
result2 = lcs_non_recursive(str1, str2)
print(result1)
print(result2)
