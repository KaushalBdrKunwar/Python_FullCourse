## Protected Variables

class Person:
    def __init__(self,name,age,gender):
        self._name = name   #protected
        self._age = age #protected
        self.gender = gender

## cannot access outside the class but can from derived class
class Employee(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

# def get_name(person):
#     return person.name

# person = Person("Krish",20,"male")
# print(get_name(person))

employee = Employee("krish",22,"male")
print(employee._name)