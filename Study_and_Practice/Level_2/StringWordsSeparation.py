# Split a sentence full of words, singular letters, special characters, numbers spaces properly into individual
# elements in a list

import re


def split_sentence(sentence):
    # Regular expression pattern to match words, digits, spaces, and special characters
    pattern = r'\d+|[a-zA-Z]+|[^\w\s]|\s'
    return re.findall(pattern, sentence)


# Input
input_sentence = "How is Mr. Hans on a 13th?"
output = split_sentence(input_sentence)
print(output)
