# FACTORY PATTERN: IS A creational design pattern that provides an interface for creating objects in a superclass,
# but allows subclasses to alter the type of objects that will be created.

import pygame
import random
from abc import ABC, abstractmethod
from enum import Enum, auto

class ShapeType(Enum):
    CIRCLE = auto()
    RECTANGLE = auto()
    TRIANGLE = auto()

class Shape(ABC):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = random.randint(10, 50)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = random.randint(20, 100)
        self.height = random.randint(20, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Triangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = random.randint(20, 100)
        self.height = random.randint(20, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [(self.x, self.y), (self.x + self.width, self.y), (self.x + self.width / 2, self.y + self.height)])

class ShapeContext:
    def __init__(self, shape_type, x, y):
        self.shape_type = shape_type
        self.x = x
        self.y = y

class ShapeFactory:
    def create_shape(self, context):
        if context.shape_type == ShapeType.CIRCLE:
            return Circle(context.x, context.y)
        elif context.shape_type == ShapeType.RECTANGLE:
            return Rectangle(context.x, context.y)
        elif context.shape_type == ShapeType.TRIANGLE:
            return Triangle(context.x, context.y)
        else:
            raise ValueError("Invalid shape type")

# Main function to set up and run the game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Random Shapes")
    clock = pygame.time.Clock()

    shape_factory = ShapeFactory()
    shapes = []  # List to store created shapes
    running = True

    # Main game loop
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Create a random shape on mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                shape_type = random.choice(list(ShapeType))
                context = ShapeContext(shape_type, x, y)
                shape = shape_factory.create_shape(context)
                shapes.append(shape)

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw all the shapes
        for shape in shapes:
            shape.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()