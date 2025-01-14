# Q - Add the fruits in the basket

def put_fruits(fruits, cart):
    for key, val in fruits.items():
        if key in cart:
            cart[key] += val
        else:
            cart[key] = val
    print(cart)


# Input
fruits = {
    "Apple": 3,
    "Banana": 4,
    "Orange": 5
}
cart = {
    "Eggs": 6,
    "Watermelon": 7,
    "Coconut": 8,
    "Apple": 1,
}
put_fruits(fruits, cart)
