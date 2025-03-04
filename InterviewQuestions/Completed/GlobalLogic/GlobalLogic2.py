# You are given a string S. You can repeatedly perform the following delete operation:
# If the string contains the substring "AB" or "BB", you can remove it from S in one operation.
# The remaining characters are concatenated to form a new string.
# And you continue this process until no further deletions are possible.
# Your task is to determine the length of the final string after performing all possible operations.


def final_string_length(s):
    stack = []

    for char in s:
        if stack and (stack[-1] == 'A' and char == 'B' or stack[-1] == 'B' and char == 'B'):
            stack.pop()  # Remove "AB" or "BB"
        else:
            stack.append(char)  # Keep adding valid characters

    return len(stack)


# Test cases
print(final_string_length("ABBAB"))
