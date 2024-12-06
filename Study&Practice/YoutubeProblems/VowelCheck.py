# List all the vowels present in a string

def vowel_check(s):
    vowel_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    vowels = [v for v in s if v in vowel_list]
    print(vowels)


s = str(input("Enter the string: "))
vowel_check(s)
