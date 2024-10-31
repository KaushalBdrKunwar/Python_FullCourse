#Write a recursive function to print sum of first n natural numbers.

def sum(n):
    if (n == 0):
        return 0
    elif(n==1):
        return 1
    else:
        return n + sum(n-1)

n = int(input("Enter the number:"))

print(f"The sum is: {sum(n)}")