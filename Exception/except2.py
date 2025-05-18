try:
    result = 1/2
    a = b
except ZeroDivisionError as z:
    print(z)
    print("Please enter the denominator greater than 0")
except Exception as ex:
    print(ex)
    print("Main exception got caught here.")