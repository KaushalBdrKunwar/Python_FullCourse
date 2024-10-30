#WAP to find whether a given username contains less than 10 
#characters or not.

username = input("Enter the username:")

lenghtname = len(username)

if(lenghtname<10):
    print("It contains less than 10 characters", lenghtname)