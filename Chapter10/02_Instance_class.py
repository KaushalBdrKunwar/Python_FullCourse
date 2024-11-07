class Employee:
    language = "Py" #this is a class attribute
    salary = 1200000


harry = Employee()
harry.name = "Harry"#this is an object(instance) attribute
harry.language = "JavaScript"
print(harry.language, harry.salary)

#instance attribute has more priority than class attribute
