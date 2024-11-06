#Rename the file.

with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\file.txt","r") as f:
    content = f.read()

with open("renamed_by_python.txt","w") as f:
    f.write(content)