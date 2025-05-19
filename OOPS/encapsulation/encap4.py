## Encapsulation with getter and setter

class Person:
    def __init__(self,name,age):
        self.__name = name #Private variable
        self.__age = age #Private variable
    
    ## getter method for name
    def get_name(self):
        return self.__name
    
    ## setter method for name in order to change the name.
    def set_name(self,name):
        self.__name = name

person = Person("Krish",34)

## Access and modify private variables using getter and setter

print(person.get_name())

person.set_name("Harry")
print(person.get_name())