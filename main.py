
from enum import Enum, auto
from abc import ABC, abstractmethod

class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"


class Vichel(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Car(Vichel):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print("car name", self.name)



class MoterCycle(Vichel):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print("Motor Cycle name", self.name)


class Bicycle(Vichel):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print("Bi Cycle name", self.name)



class VichelContext:
    
    def __init__(self,context, name):
        self.context = context
        self.name = name


class VechileFactory:
    @staticmethod
    def create_vehicle(context, name):
        if context == VehicleType.CAR:
            return Car(name)
        elif context == VehicleType.MOTORCYCLE:
            return MoterCycle(name)
        elif context == VehicleType.BICYCLE:
            return Bicycle(name)
        else:
            raise ValueError("Not defined")


if __name__ == "__main__":
    vehicle_factory = VechileFactory()

    # Test the VehicleFactory by creating different types of vehicles
    car = vehicle_factory.create_vehicle(VehicleType.CAR, "Toyota")
    print(car.get_name())