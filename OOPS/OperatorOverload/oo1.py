## Operator Overloading..
## It allows us to define the behavior of operators(+,-,*,etc.) for custom objects. 
# Common operator overloading magic method:
# __add__(self,other): Adds two objects using + operator.
# __sub__(self,other): Subtracts two objects using the - operator.
# __mul__(self,other): Multiplies two obje using *
# __truediv__(self,other): Divides two objs using / operator.
# __eq__(self,other): checks if two objs are equal using ==.
#__lt__(self,other): Checks if one objs is less than another using the < operator.
#__gt__(self,other): Checks if one objs greater less than another using the >operator.

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
        return Vector(self.x*other.x,self.y*other.y)
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f" Vector({self.x}, {self.y})"

## create objects of vector class
v1 = Vector(2,3)
v2 = Vector(4,5)

print(v1+v2)
print(v1-v2)
