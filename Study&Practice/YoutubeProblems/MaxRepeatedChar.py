# Find max repeated character in a string

def max_repeat(s):
    ch = {}

    for char in s:
        if char in ch:
            ch[char] += 1
        else:
            ch[char] = 1

    max_char = max(ch, key=ch.get())
    print(max_char)


# Input
s = str(input("Enter a string: "))
max_repeat(s)
