# Q - Compare the two given strings and give observations on which ones are added, deleted, replaced and inserted

def compare_strings(str1, str2):
    # Split the strings into words
    words1 = str1.split()
    words2 = str2.split()

    # Create sets for easy comparison
    set1 = set(words1)
    set2 = set(words2)

    # Find added and deleted words
    added = list(set2 - set1)
    deleted = list(set1 - set2)

    # Find replaced words (order mismatch)
    replaced = []
    for word1, word2 in zip(words1, words2):
        if word1 != word2:
            replaced.append((word1, word2))

    # Handle case where one string is longer
    if len(words1) < len(words2):
        replaced.extend((None, word2) for word2 in words2[len(words1):])
    elif len(words1) > len(words2):
        replaced.extend((word1, None) for word1 in words1[len(words2):])

    print(f"Added: {added}")
    print(f"Deleted: {deleted}")
    print(f"Replaced: {replaced}")


# Input
str1 = "my name is ESWARA"
str2 = "My naam is ESWARA okay"
compare_strings(str1, str2)
