#4. Add static method in problem 2, to greet the user with hello.

class calculator:
    def __init__(self, n):
        self.n =n
    
    def square(self):
        print(f"The square is {self.n*self.n}")
    
    @staticmethod
    def greet():
        print("hello")
    

a = calculator(4)
a.square()
a.greet()