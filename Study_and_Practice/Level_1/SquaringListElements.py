# Square the elements of the list individually

def square_elements(numbers):
    square_numbers = [number**2 for number in numbers]
    print(square_numbers)


numbers = list(map(int, input("Enter the elements in the list to be squared with space separation: ").split()))
square_elements(numbers)
