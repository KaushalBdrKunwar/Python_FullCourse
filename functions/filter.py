# The filter() function constructs an iterator from elements of an iterable for which a function returns true. 
# It is used to filter out items from a list(or any other iterable) based on condition.


def even(num):
    if num%2 == 0:
        return True

print(even(24))

lst = [1,2,3,4,5,6,7,8,9,10]

even_values = list(filter(even,lst))
print(even_values)

## filter with a lambda function
greater_than_five = list(filter(lambda x:x >5, lst))
print(greater_than_five)

even_and_greater_than_five = list(filter(lambda x:x>5 and x%2==0, lst))
print(even_and_greater_than_five)

## Filter to check if the age is greater than 25 in dictionaries
people=[
    {'name': 'Krish', 'age':'32'},
    {'name': 'Hari', 'age':'30'},
    {'name': 'Madan', 'age':'20'},
]

def age_greater_than_25(person):
    return int(person['age'])>25

old_people = list(filter(age_greater_than_25,people))
print(old_people)

# It is commonly used in data cleaning, filtering objects, and removing unwanted element from lists.
