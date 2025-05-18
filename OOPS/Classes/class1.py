### A class is a blue print for creating objects. Attributes, methods
class Car:
    pass

audi = Car()
bmw= Car()

print(type(audi))

### Modeling a bank account.
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} is deposited. New balance is {self.balance}")
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn. New Balance is {self.balance}")
    
    def get_balance(self):
        # print(f"Your balance is {self.balance}")
        return self.balance

## create an account

account = BankAccount("Kaushal",5000)
print(account.balance)

# Call instance methods
new_balance = account.deposit(100)
print(new_balance)

afterWithdrawn = account.withdraw(10)
print(afterWithdrawn)

print(account.get_balance())