f = open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\poem.txt")
content = f. read()
if("twinkle" in content):
    print("The word is present in content")
else:
    print("Not present")
f.close()