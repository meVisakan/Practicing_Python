# Get the first non repeating character from a string

def non_rep(my_str):
    if len(my_str) > 1:
        s_dict = {}
        for char in my_str:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        for key, value in s_dict.items():
            if value == 1:
                return key
        return "All repeating characters"
    else:
        return "Enter a proper string"


# Input
my_str = str(input("Enter a string: "))
print(non_rep(my_str))
