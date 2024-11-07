class Employee:
    language = "Py" #this is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")


harry = Employee()
harry.name = "Harry"#this is an object(instance) attribute
harry.language = "JavaScript"
print(harry.language, harry.salary)
harry.getInfo()
harry.greet()

