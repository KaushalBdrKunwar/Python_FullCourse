
## Multiple Inheritance
# When a class from more than one base class

#Base Class1:
class Animal:
    def __init__(self,name,language):
        self.name = name
        self.language = language
    
    # def speak(self):
    #     print(f"The {self.name} does {self.language} sound.")

# dog = Animal("Dog","Barks")

# dog.speak()

## Base class2
class Pet:
    def __init__(self,owner):
        self.owner = owner

## Derived class
class Dog(Animal,Pet):
    def __init__(self, name, language,owner):
        # super().__init__(name, language,owner)
        Animal.__init__(self,name,language)
        Pet.__init__(self,owner)
    
    def speak(self):
        print(f"The {self.name} owned by {self.owner} says {self.language}")

dog = Dog("Dog","Woof","John")
dog.speak()