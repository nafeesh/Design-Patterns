# Liskov Substitution Principle
# Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.

# example 1: without LSP

class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")


def make_bird_fly(bird):
    bird.fly()

# example 2: with LSP

class Bird:
    def fly(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        print("Bird is flying")

class NonFlyingBird(Bird):
    def fly(self):
        print("Bird cannot fly")

class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(NonFlyingBird):
    def fly(self):
        print("Ostrich cannot fly")

