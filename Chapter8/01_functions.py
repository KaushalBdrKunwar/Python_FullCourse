# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))



# average = (a+b+c)/3

# print(average)

#USING FUNCTIONS:

def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a+b+c)/3
    print(average)

def even_or_odd(num):
    if num%2==0:
        print(f"The number{num} is even")
    else:
        print(f"The number{num} is odd")

a = int(input("Enter the number you want to check:"))
even_or_odd(a)

avg()
avg()
avg()
avg()

