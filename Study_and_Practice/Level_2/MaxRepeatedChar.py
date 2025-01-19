# Find max repeated character in a string

def max_rep(sent):
    char_count = {}
    max_chars = []
    for char in sent:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    maxx = max(char_count.values())

    for key, val in char_count.items():
        if val == maxx:
            max_chars.append(key)
    print(max_chars)


# Input
sent = str(input("Enter the sentence to be checked: "))     # Hellooo
max_rep(sent)
