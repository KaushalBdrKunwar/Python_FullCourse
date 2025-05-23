## Custom exception (Raise and Throw an exception)

class Error(Exception):
    pass

class dobException(Error):
    pass

year = int(input("Enter the birth year in AD: "))
age = 2025-year

try:
    if age<=30 and age>=20:
        print("The age is valid so you can apply for the exam.")
    else:
        raise dobException

except dobException:
    print("Sorry, your is not valid")