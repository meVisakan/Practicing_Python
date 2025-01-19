class MyClass:
    class_variable = "Class Variable"

    def instance_method(self):
        return "Instance method", self

    @classmethod
    def class_method(cls):
        return "Class method", cls.class_variable

    @staticmethod
    def static_method():
        return "Static method"


obj = MyClass()
print(obj.instance_method())
print(MyClass.class_method())
print(MyClass.static_method())
