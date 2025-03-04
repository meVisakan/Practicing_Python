# Given a string, return the first recurring character in it, or "None" if there is no recurring character.

def first_recurring_character(s):
    seen = set()

    for char in s:
        if char in seen:
            return char
        seen.add(char)

    return "None"


# Input
s = str(input("Enter a string: "))
print(first_recurring_character(s))
