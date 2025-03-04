s = "()[]{}"
s = "(())"


def bracket_check(s):
    brackets = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for i in s:
        if i in stack:
            pass
        else:
            stack.append(i)
    print(stack)

    if len(stack) != 0:
        return False
    return True


bracket_check(s)
