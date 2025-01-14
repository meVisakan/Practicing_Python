# Get the indexes of anagram words from a list

def anagram_index(wrds):
    if len(wrds) > 1:
        w_list = wrds.split(" ")
        print(w_list)
        w_dict = {}
        for i in range(len(w_list)):
            temp = ''.join(sorted(w_list[i]))
            if temp not in w_dict:
                w_dict[temp] = [i]
            else:
                w_dict[temp].append(i)
        result = {key: val for key, val in w_dict.items() if len(val) > 1}
        print("The present anagrams with their indexes are: ", result)
    else:
        print("Invalid Input!")


# Input
wrds = str(input("Enter the words to check for the indexes of their anagrams: "))
anagram_index(wrds)

