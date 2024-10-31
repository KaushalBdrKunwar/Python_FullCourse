#WAP to find sum of n numbers:

n = int(input("Enter the number upto where sum is required:"))

i = 0
sum =0
while(i<=n):
    sum = i + sum 
    i += 1

print("The sum is:",sum)
