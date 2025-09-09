# Base class
class Shape:
    def __init__(self, name):
        # Initialization logic from the base class
        self.name = name
        print(f"Shape '{self.name}' initialized.")

    def calculate_area(self):
        # This method can be empty or have a default behavior
        print("Calculating area from the base Shape class.")

# Derived class
class Rectangle(Shape):
    def __init__(self, name, length, width):
        # Use super() to call the constructor of the base class (Shape)
        super().__init__(name)
        self.length = length
        self.width = width

    def calculate_area(self):
        # Overriding the method from the base class
        # You could also call super() here if needed for shared logic
        return self.length * self.width

# Example usage
rectangle = Rectangle("My Rectangle", 10, 5)
print(f"The area of the rectangle is: {rectangle.calculate_area()}")