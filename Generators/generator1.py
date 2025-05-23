## iterator using generator

# def square(n):
#     for i in range(n):
#         return i**2
def square(n):
    for i in range(n):
        yield i**2

print(square(3)) # Now this is generator because of yeild

for i in square(3):
    print(i)