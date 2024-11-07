#Create a class with a class attribute a; create an object from it and set
#'a' directly using object.a = o. Does this change class attribute?

class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not present


o.a = 0
print(o.a)#prints the instance attribute because its present

