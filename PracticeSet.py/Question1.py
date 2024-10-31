#WAP to print table of given number using loop:

num = int(input("Give the number:"))

for i in range(1,11):
    a = num * i
    print(num,"*",i,"=",a)
    