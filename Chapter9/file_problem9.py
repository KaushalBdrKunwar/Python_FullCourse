#WAP to show that the two files are identical

with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\file1.txt") as f:
    content1 = f.read()

with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\file2.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("The files are identical")
else:
    print("The files are not identical")