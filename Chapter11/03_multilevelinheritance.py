class Employee:
    company = "Infosis"

    def getInfo(self):
        print(f"The employees are from {self.company}")


class Programmer(Employee):
    language = "Python"

    def getLanguage(self):
        print(f"The employee know {self.language}")

class Manager(Programmer):
    print("I know everything.")

m = Manager()

m.getInfo()
m.getLanguage()