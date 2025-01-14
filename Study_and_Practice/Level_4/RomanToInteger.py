# Convert a given roman numeral to integer

def roman_int(rom):
    result = 0
    n = len(rom)
    for i in range(n):
        if i < n-1 and value(rom[i]) < value(rom[i+1]):
            result -= value(rom[i])
        else:
            result += value(rom[i])

    return result


def value(val):
    if val == 'I':
        return 1
    if val == 'V':
        return 5
    if val == 'X':
        return 10
    if val == 'L':
        return 50
    if val == 'C':
        return 100
    if val == 'D':
        return 500
    if val == 'M':
        return 1000


# Input
rom = str(input("Enter the Roman numeral as a string: "))
print(roman_int(rom))
