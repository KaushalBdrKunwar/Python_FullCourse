# a = b name error as b is not defined

## Exception try, except block

# try:
#     a=b 
# except:
#     print("The variable has not been assigned")

try:
    a=b 
except NameError as ex:
    print(ex)