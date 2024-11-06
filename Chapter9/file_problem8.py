#WAP to make copy of a text file "this.txt"

with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\this.txt") as f:
    content = f.read()

with open("this_copy.txt","w") as f:
    f.write(content)



