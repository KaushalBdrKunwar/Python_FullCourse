#WAP to print first n lies in following pattern:
# '''
# ***
# **
# *

# '''

# n = int(input("Enter the number:"))

# for i in range(1,n+1):

#     print("*"*n)
#     n = n-1

#--------------USING----FUNCTION---------#

def pattern(n):
    if(n==0):
        return ""

    print("*"*n)
    pattern(n-1)

num = int(input("Enter the number:"))

pattern(num)