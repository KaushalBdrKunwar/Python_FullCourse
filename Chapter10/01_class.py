class Employee:
    language = "Py" #this is a class attribute
    salary = 1200000


harry = Employee()
harry.name = "Harry"#this is an object(instance) attribute
print(harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.salary,rohan.language)

# Here name is object attribute and salaray and language are
# class attributes as they directly belong to the class