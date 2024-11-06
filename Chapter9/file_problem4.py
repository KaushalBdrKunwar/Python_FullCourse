#A file contains a word "Donkey" multiple times. You need to WAP which
#replaces this word with "#####" by updating the same file.

word = "Donkey"

with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\filedon.txt","r") as f:
    content = f.read()

contentNew = content.replace(word,"######")

with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\filedon.txt","w") as f:
    content = f.write(contentNew)