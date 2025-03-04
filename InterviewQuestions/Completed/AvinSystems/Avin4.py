class Father:
    def speak_loud(self):
        print("Father Speaking Loudly")


class Mother:
    def speak_soft(self):
        print("Mother Speaking Softly")

    def speak_loud(self):
        super().speak_loud()
        print("Mother Speaking Loudly")


class Child(Father, Mother):
    def talk(self):
        print("Child Talking")


my_child = Child()
my_child.speak_loud()
my_child.speak_soft()
my_child.talk()
