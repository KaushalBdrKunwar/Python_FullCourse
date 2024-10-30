#A spam comment is defined as a text containing following keywords:
#"Make a lot of money", "Buy now", "subscribe this", "click this".
#WAP to detect spam.

# spam = input("Enter spam message:")

# if(spam =="Make a lot of money" or spam =="Buy now"
#    or spam=="subscribe this" or spam =="click here"):
#     print("Spam detected:",spam)
# else:
#     print("It is not a spam",spam)

p1 = "Make a lot of money"
p2 = "Buy now"
p3 ="click here"
p4= "subscribe this"

message = input("Enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam",message)