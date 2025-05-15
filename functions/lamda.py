# Lamda functions are small anonymous functions defined using lamda keyword. They can have any number of arguments but only one expression. They are commonly used for short operations or as arguments to higher-order functions.

#syntax : lambda arguments: expression

def addition(a,b):
    return a+b

addition(2,3)

## or 

add = lambda a,b : a+b # add is lambda function

print(add(5,6))

## map() - applies a function to all items in a list
numbers = [1,2,3,4,5]
square = map(lambda x:x**2,numbers) # no need to iterate through all the elements of list through loops
print(square)
