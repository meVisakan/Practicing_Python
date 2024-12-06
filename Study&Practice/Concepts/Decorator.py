# Decorator is a special kind of function that adds extra functionality to another function.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function")
        func()
        print("Something is happening after the function")
    return wrapper


@my_decorator
def say_hello():
    print("Hello")


say_hello()
