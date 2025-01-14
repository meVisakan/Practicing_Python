# Filter function takes a function object and an iterable and creates a new list.

fruit = ['Apple', "Banana", "Apricot", "Mango"]
filter_object = filter(lambda s: s[0] == "A", fruit)
print(list(filter_object))
