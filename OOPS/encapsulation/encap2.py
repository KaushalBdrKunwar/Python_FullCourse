class Person:
    def __init__(self,name,age,gender):
        self.__name = name # Instance variables are private
        self.__age = age # Private variables
        self.gender = gender # Public

# def get_name(person):
#     return person.__name This wont be executed because of private variable.

def get_name(person):
    return person._Person__name # Copying from dir which is not good practice


person = Person("Krish", 34, "Male")
print(dir(person))

get_name(person)