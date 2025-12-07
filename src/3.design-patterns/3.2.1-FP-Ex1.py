from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"

# Step 1: Create an abstract Animal class
class Animal(ABC):
    def __init__(self, data: dict):
        self.name = data.get('name', 'Unknown')
        self.age = data.get('age', 0)
    
    @abstractmethod
    def get_info(self) -> str:
        pass

# Step 2: Create concrete animal classes
class Dog(Animal):
    def get_info(self) -> str:
        return f"Woof! I am a Dog named {self.name}, aged {self.age}."

class Cat(Animal):
    def get_info(self) -> str:
        return f"Meow! I am a Cat named {self.name}, aged {self.age}."

class Fish(Animal):
    def get_info(self) -> str:
        return f"Blub! I am a Fish named {self.name}, aged {self.age}."

# Step 3: Create an AnimalFactory class
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        if animal_type == AnimalType.DOG:
            return Dog(context)
        elif animal_type == AnimalType.CAT:
            return Cat(context)
        elif animal_type == AnimalType.FISH:  # Fixed: Match Enum member name
            return Fish(context)
        else:
            raise ValueError(f"Animal type {animal_type} is not supported.")

# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()

    # Test 1: Create a Dog
    dog_context = {"name": "Buddy", "age": 3}
    dog = animal_factory.create_animal(AnimalType.DOG, dog_context)
    print(dog.get_info())

    # Test 2: Create a Fish
    fish_context = {"name": "Nemo", "age": 1}
    fish = animal_factory.create_animal(AnimalType.FISH, fish_context)
    print(fish.get_info())

if __name__ == "__main__":
    main()