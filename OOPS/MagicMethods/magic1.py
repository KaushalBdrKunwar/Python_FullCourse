## Magic Methods in Python:
## it is also known as dunder methods(double underscore methods) are special methods that
## start and end with double undersocers. To define behaviour of objects for built in operations
## eg. arithematic operations, comparisons, and more.

## they are predefined methods in python that you can override to change the behaviour
## of your objects. Some common magic methods are:

## 1.__init__: initializes new instance of class.
## 2.__str__: Returns a string representation of an object.
## 3__repr__: Returns an official string representation of an object.
## 4__getitem__: Gets an item from a container.
## 5.__setitem__: Sets an item in a container.
## 6.__len__: Returns length of an object.

class Person:
    pass

person = Person
# print(dir(person))

## Basic Methods
class Man:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name},{self.age} years old"

man = Man("Krish",34)
print(man)