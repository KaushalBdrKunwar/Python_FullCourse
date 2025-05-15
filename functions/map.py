def square(x):
    return x*x

# square(10)  ## for 10 only.

numbers = [1,2,3,4,5,6,7,8]

after_map = list(map(square,numbers))
print(after_map)

## Map multiple iterables

numbers1 = [1,2,3]
numbers2 = [4,5,6]

added_numbers = list(map(lambda x,y: x+y, numbers1,numbers2))
print(added_numbers)

## map() to convert list of strings to integers
str_numbers = ['1','2','3']
int_numbers = list(map(int, str_numbers))

print(int_numbers)

## map() to convert to uppercase
words = ['apple', 'banana', 'mango']
upper_words = list(map(str.upper, words))
print(upper_words)

