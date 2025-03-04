# Run-Length Encoding (RLE) for a given string.
# It will also separate out the characters that cannot be encoded (like numbers or special characters)

def run_length_encoding(s):
    encoded_str = ""
    non_encoded_str = ""

    if len(s) == 0:
        print("Enter characters in the string!")
    else:
        i = 0
        while i < len(s):
            # If the character is an alphabet, we will apply RLE
            if s[i].isalpha():
                count = 1   # Initialize count for the character
                # Count consecutive occurrences of the same letter
                while i+1 < len(s) and s[i] == s[i+1]:
                    count += 1
                    i += 1
                # Append the count and character to the encoded string
                encoded_str += str(count) + s[i]
            # Non-alphabetical characters are added directly to non_encoded_str
            else:
                non_encoded_str += s[i]

            i += 1  # To keep the loop going regardless of non-alphabetical characters

        if len(encoded_str) == 0:
            print("No characters to be encoded")
            print("Non-encoded String: ", non_encoded_str)
        elif len(non_encoded_str) == 0:
            print("All characters to be encoded")
            print("Encoded String: ", encoded_str)
        else:
            print("Encoded String: ", encoded_str)
            print("Non-encoded String: ", non_encoded_str)


# Input
s = input("Enter the string to be encoded: ")
run_length_encoding(s)
