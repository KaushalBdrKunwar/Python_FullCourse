class Employee:
    def __init__(self):
        print("Constructor of Employee")

    company = "Infosis"

    def getInfo(self):
        print(f"The employees are from {self.company}")


class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")

    language = "Python"

    def getLanguage(self):
        print(f"The employees know {self.language}")

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")

    print("I know everything.")

m = Manager()

m.getInfo()
m.getLanguage()