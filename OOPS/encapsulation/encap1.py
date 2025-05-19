### Encapsulation with Getter and Setter Methods
### Public,protected, private variables

class Person:
    def __init__(self,name,age):
        self.name = name # Instance variables are public
        self.age = age # Public variables

def get_name(person):
    return person.name


person = Person("Krish",34)
print(person.name)

# print(dir(person))