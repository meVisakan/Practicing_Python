def run_length_encoding(s):
    l = len(s)
    encoded_str = ""
    non_encoded_str = ""

    if l > 1:
        i = 0
        while i < l:
            if s[i].isalpha():
                count = 1
                while i+1 < l and s[i] == s[i+1]:
                    count += 1
                    i += 1
                encoded_str += str(count) + s[i]
            else:
                non_encoded_str += s[i]
    else:
        print("Invalid Input!")


# Input
s = str(input("Enter the string to be encoded: "))
run_length_encoding(s)
