class Father:
    def speak_loud(self):
        print("Father speaking loudly")


class Mother:
    def speak_soft(self):
        print("Mother speaking softly")

    def speak_loud(self):
        print("Mother speaking loudly")


class Child(Father, Mother):
    def talk(self):
        print("Child talking")


my_child = Child()
my_child.speak_soft()
my_child.speak_loud()
my_child.talk()
