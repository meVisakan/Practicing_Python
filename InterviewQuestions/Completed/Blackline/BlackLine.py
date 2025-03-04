# Q - Get the count of the characters in a string

def char_count(q_str):
    count = {}
    for i in q_str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)


# Input
q_str = str(input("Enter a string: "))
char_count(q_str)
