class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
