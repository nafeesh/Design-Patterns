# Open-Closed Principle
# Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

# example 1: without OCP
# This code violate OCP because if we want to add new shape, we have to modify the code.

class AreaCalculator:

    def area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius * shape.radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


# example 2: with OCP
# This code doesn't violate OCP because if we want to add new shape, we don't have to modify the code.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def area(self, shape):
        return shape.area()