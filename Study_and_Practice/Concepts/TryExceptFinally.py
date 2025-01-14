try:
    num = int(input("Enter an integer: "))  # this could get ValueError
    print(f"You entered: {num}")
except ValueError:
    print("That's not a valid number")
finally:
    print("Executed no matter what")
