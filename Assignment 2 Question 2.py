import math

# Base class for shapes (optional but good practice)
class Shape:
    def calculate_area(self):
        pass

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        # The function calls the correct calculate_area() method based on the shape's type
        total_area += shape.calculate_area()
    return total_area

# Example usage with a list of different shapes
shapes = [
    Circle(10),
    Rectangle(5, 8),
    Circle(5),
    Rectangle(10, 4)
]

print(f"The total area of all shapes is: {calculate_total_area(shapes)}")