# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        return f"This is a {self.brand} {self.model}."

# Subclass inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    # Override the describe() method
    def describe(self):
        return f"This is a {self.brand} {self.model} with {self.num_doors} doors."

# Subclass inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    # Override the describe() method
    def describe(self):
        return f"This is a {self.brand} {self.model} which is a {self.bike_type} bike."

# Example usage with all classes present
car = Car("Ford", "Ranger Raptor", 4)
bike = Bike("Trek", "Marlin", "mountain")

print(car.describe())
print(bike.describe())