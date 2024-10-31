#WAP to write a table using for loop in reverse order

n = int(input("Enter the number:"))

for i in range(1,11):
    print(f"{n} * {11 - i} = {n*(11-i)}")