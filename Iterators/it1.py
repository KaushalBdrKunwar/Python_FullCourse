# Iterators are advanced Python concepts that allow for efficient looping and
# memory management. Iterators provide a way to access elements of a collection sequentially
# without exposing the underlying structure.

my_list = [1,2,3,4,5,6]

print(type(my_list))

#normal approach
for i in my_list:
    print(i)

# ## Iterator
# iterator = iter(my_list)
# print(type(iterator))

# # Iterate through all the element
# ## Performs lazy loading so gives output only 1 that is one at  a time
# # next is a inbuilt function
# print(next(iterator))

# ## Iterator
iterator = iter(my_list)

try:
    print(next(iterator))
except StopIteration:
    print("There is no elements in the iterator")

### can be used for string also in the same way.
