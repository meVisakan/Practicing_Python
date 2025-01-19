class Relation:
    def __init__(self, name, msg):
        self.name = name
        self.msg = msg


# Creating an object which calls the constructor
relation = Relation("VE", "got this")
print(relation.name + " " + relation.msg)
