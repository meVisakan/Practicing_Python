# Count the total number of capital letters in a file

def count_capitals():
    count = 0
    with open("file.txt", 'r') as file:
        for line in file:
            for char in line:
                if char.isupper():
                    count += 1
    print("Number of capital letters in the file: ", count)

    # sum(l for line in open("file.txt") for char in line if char.isupper())    1-line code

    
count_capitals()
