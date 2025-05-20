## Abstraction is the concept of hiding the complex implementation details and showing
## only the necessary features of an object. This helps in reducing programming complexity and effort.

from abc import ABC,abstractmethod

## Abstract base class
class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving")
    
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car enginee started")

def operate_vehicle(vehicle):
    vehicle.start_engine()

car = Car()
operate_vehicle(car)