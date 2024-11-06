

with open(r"C:\Users\legion\Desktop\PythonFullCourse\Chapter9\log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line ):
        print(f"Yes there is python. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No python is present")