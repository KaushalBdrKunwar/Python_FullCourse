#WAP to print a dictionary of Nepali words with values as 
#their English Translation. Provide user with an option 
#to look up!

words = {
    "ama": "mother",
    "Baba" : "Father",
    "Vai" : "Brother",
    "didi" : "sister"
}

word = input("enter the word you want meaning of:")

print(words[word])