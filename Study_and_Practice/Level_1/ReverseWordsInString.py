# Reverse the words individually in a string as well as the whole string
# Same as s[::-1]

def words_reversed(s):
    words = s.split(" ")
    rev_order = words[::-1]
    print("Rev order of words in string: ", rev_order)
    for i in range(len(rev_order)):
        rev_order[i] = rev_order[i][::-1]
    output_s = ' '.join(rev_order)
    print("Entire string reversed: ", output_s)


s = input("Enter a string whose words need to be reversed: ")
words_reversed(s)
