# Basic file operations
# Code shall give error on execution as no such file is present

# Open file in read mode
with open("exam.txt", "r") as file:
    content = file.read()   # Reads entire content of the file
    print(content)

    line = file.readline()   # Reads the first line
    while line:
        print(line.strip())   # Remove any extra whitespace and print
        line = file.readline()   # Read the next line

    lines = file.readlines()    # Reads all lines into a list
    for line in lines:
        print(line.strip())


with open("exam.txt", "w") as file:
    file.write("Hello!\n")


with open("exam.txt", "a") as file:
    file.write("This line is to be added.\n")
