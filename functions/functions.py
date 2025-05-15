### Variable Length Arguments
## Positional and Keywords arguments

### positional args.
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1,2,3,4,5,6,"Krish")

### Keywords Arguments

def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    
print_details(name="krish",age="32",country="Nepal")