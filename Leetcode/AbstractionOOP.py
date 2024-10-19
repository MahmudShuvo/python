from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started."

# Usage
vehicles = [Car(), Motorcycle()]
for vehicle in vehicles:
    print(vehicle.start_engine())
