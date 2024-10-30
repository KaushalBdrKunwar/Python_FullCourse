#Create an empty dictionary. Allow 4 friends to enter their favorite
#language as value and use key as their names. Assume that the names
#are unique.

language ={}

name = input("Enter friends name: ")
lang = input("Enter language name: ")

language.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")

language.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
language.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")

language.update({name: lang})

print(language)
