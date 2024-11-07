#1.Create a Class "Programmer" for storing information of few programmers 
#working at microsoft

class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Harry", 1200000, 254672)

print(p.name,p.salary,p.salary)