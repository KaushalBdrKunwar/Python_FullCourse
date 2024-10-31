#WAP using function to convert Celsius to Fahernheit.

def Conversion(Celcius):
    Fahernheit = Celcius*(9/5)+32
    print(f"The Temperature is: {Fahernheit}")

c = int(input("Enter temperature in celcius:"))
Conversion(c)
