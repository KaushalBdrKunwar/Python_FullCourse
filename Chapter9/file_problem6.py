#WAP to detect python in the file log.txt.

with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\log.txt") as f:
    content = f.read()

if("python" in content ):
    print("Yes there is python.")
else:
    print("No there isnt python.")