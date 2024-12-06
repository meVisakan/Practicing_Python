class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.model} engine started in {self.year}"


# Creating an object (instance of the Car class)
my_car = Car("Hyundai", 2023)
print(my_car.start_engine())
