try:
    num = int(input("Enter a number"))
    div = 10/num

except ValueError as v:
    print(v)
    print("Please enter a correct number.")

except ZeroDivisionError as z:
    print(z)
    print("Enter number greater than zero.")

except Exception as ex:
    print(ex)

