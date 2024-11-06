#WAP to cnesor the words in mine file.

words = ["python","bad","Donkey"]

with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\mine.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,f"{"#"*len(word)}")

with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\mine.txt","w") as f:
    f.write(content)
