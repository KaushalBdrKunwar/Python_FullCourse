## 2. Polymorphism with Abstract Base class(Interface.)

from abc import ABC, abstractmethod

## Define an abstract class
### ABC is an empty class itself with empty mehtod initially.
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Derived class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car enginee started"

# Derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle enginee started"

## Function that defines polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())

### create objects of car and motorcycle

car = Car()
motorcycle = Motorcycle()

start_vehicle(car)