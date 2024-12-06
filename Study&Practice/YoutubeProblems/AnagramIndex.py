# Get the indexes of anagram words from a list

def anagram_index(w_list):
    if len(w_list) > 1:
        w_dict = {}
        for i in range(len(w_list)):
            temp = ''.join(sorted(w_list[i]))
            if temp not in w_dict:
                w_dict[temp] = [i]
            else:
                w_dict[temp].append(i)
        print(w_dict)
    else:
        print("Enter a proper word list!")


# Input
w_list = list(map(str, input("Enter the words with space separation: ").split()))
anagram_index(w_list)
