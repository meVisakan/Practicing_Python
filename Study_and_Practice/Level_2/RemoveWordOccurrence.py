# Remove the word on its nth occurrence

def remove_word(sentence, word, n):
    slist = sentence.split(" ")
    count = 0
    word = word.lower()

    for w in range(len(slist)):
        if slist[w].lower() == word:
            count += 1
            if count == n:
                del slist[w]
                return " ".join(slist)
    return "Word is not present!"


# Input
sentence = str(input("Enter the string with the words: "))
word = str(input("Enter the word for removal: "))
n = int(input("Enter the occurrence for removal: "))
print(remove_word(sentence, word, n))
