# Draw star pattern

def pattern_1(**kwargs):
    for i in range(r):
        for j in range(i+1):
            print(char, end=" ")
        print()


# Input
r = int(input("Enter the number of rows: "))
char = str(input("Enter the character to be printed: "))
pattern_1(r=r, char=char)
