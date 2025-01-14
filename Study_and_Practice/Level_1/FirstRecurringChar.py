# Given a string, return the first recurring character in it, or "None" if there is no recurring character.

def first_recurring_character(st):
    seen = set()

    for char in st:
        if char in seen:
            return char
        seen.add(char)

    return "None"


# Input
st = str(input("Enter a string: "))
print(first_recurring_character(st))
