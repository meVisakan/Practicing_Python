# Given a string s containing just the characters '(', ')', '{', '}', '[', ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

def valid_parenthesis(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop()
            if not stack or top_element != mapping[char]:
                return False
        else:
            stack.append(char)
    print(not stack)


# Input
s = str(input("Enter a parenthesis string: "))
valid_parenthesis(s)
