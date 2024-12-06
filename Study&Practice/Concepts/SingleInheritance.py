# Single Inheritance is when a class inherits from a single superclass.

# Parent class
class Parent:
    def speak(self):
        print("Parent Speaking")


# Child class inheriting Parent class
class Child(Parent):
    def talk(self):
        print("Child Talking")


# Creating an object of Child class
child = Child()
child.speak()
child.talk()
