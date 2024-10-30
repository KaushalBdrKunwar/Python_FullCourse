a = int(input("Enter your age: "))

#If statement no: 1

if(a%2 == 0):
    print("a is even")


#If statement no: 2    

if(a>=18):
    print("You are above the age of consent")
    print("good for you!")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0")
    
else:
    print("You are below the age of consent")

print("End of Program")