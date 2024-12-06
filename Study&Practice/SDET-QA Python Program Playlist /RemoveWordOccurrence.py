# Remove the word on it's nth occurrence

def remove_word_occurrence(arr, word, n):
    count = 0
    for i in range(len(arr)):
        if arr[i] == word:
            count += 1
            if count == n:
                del arr[i]
    print("Update list: ", arr)


# Input the list of words, word to be deleted and the occurrence for deletion
arr = list(input("Enter the words to be added in the array with space separated: ").split())
word = input("Enter the word to be removed: ")
n = int(input("Enter the occurrence for removal: "))
print("Input array: ", arr)
remove_word_occurrence(arr, word, n)
