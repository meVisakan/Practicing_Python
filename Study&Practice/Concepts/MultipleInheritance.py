# Multiple inheritance is when a class can inherit from more than one superclass.

# First Parent class
class Mother:
    def speak_soft(self):
        print("Mother speaking softly")


# Second Parent class
class Father:
    def speak_loud(self):
        print("Father speaking loudly")


# Child class inheriting Parent classes
class Child(Mother, Father):
    def talk(self):
        print("Child Talking")


# Creating an object of Child class
child = Child()
child.speak_soft()
child.speak_loud()
child.talk()
print(Child.mro())  # The MRO is determined by the C3 linearization algorithm, which Python follows internally


# Multiple inheritance is when a class inherits from more than one base class.
# Python uses the Method Resolution Order (MRO) to determine which method to call when there are conflicts.
# The super() function and the MRO can help resolve conflicts.
