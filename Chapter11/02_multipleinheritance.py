class Employee:
    name = "Default name"
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
        
# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
        
#         def showLanguage(self):
#             print(f"The name is{self.name} and he is good with {self.language} Language")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee, Coder):
    company = "IIC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()