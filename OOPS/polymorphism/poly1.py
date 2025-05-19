### Method Overriding

## Base Class

class Animal:
    def speak(self):
        return "Sound of the animal"

## Derived Class
class Dog(Animal):
    def speak(self):
        return "Woof!"

## Derived Class
class cat(Animal):
    def speak(self):
        return "Meow!"


## Function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)

### 1.Polymorphism with Functions and Methods
class Shape:
    def area(self):
        return "The area of the figure."

## Derived class 1
class Rectange(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

## Derived class 2
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.12*(self.radius**2)

### Function that demonstrates polymorphism:
def print_area(shape):
    print(f"The area of shape is :{shape.area()}")

circle = Circle(3)
print_area(circle)