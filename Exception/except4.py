## try,except,else block
try:
    num=int(input("Enter a number:"))
    result= 10/num

except ValueError as v:
    print("Put the correct value of number")

except ZeroDivisionError as z:
    print("Use number grerater than 10")
except Exception as ex:
    print(ex)

else:
    print(f"the result is {result}")

### try except else and finally

try:
    num=int(input("Enter a number:"))
    result= 10/num
except ValueError as v:
    print("Put the correct value of number")
except ZeroDivisionError as z:
    print("Use number grerater than 10")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}") # exception should not be there for this
finally:
    print("Excecution complete.") # It has to excecute whether error is comming or not.
