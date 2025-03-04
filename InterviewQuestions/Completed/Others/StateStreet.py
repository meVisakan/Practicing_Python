def reverse_name(name):
    result = name[::-1]

    result2 = ''
    for i in name:
        result2 = i + result2

    print(result)
    print(result2)


# Input
name = 'Eswar'
reverse_name(name)
