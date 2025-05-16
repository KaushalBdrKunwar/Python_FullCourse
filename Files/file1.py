### Read a Whole File.
with open(r"C:/Users/legion/Desktop/PythonFullCourse/Files/example.txt") as f:
    content = f.read()
    print(content)

## Read a  file line by line
with open(r"C:/Users/legion/Desktop/PythonFullCourse/Files/example.txt") as f:
    for line in f:
        print(line.strip())# removes new line character by .strip

## Writing a File(overwrite)
a = "\n Write what you want? \n"
# with open(r"C:/Users/legion/Desktop/PythonFullCourse/Files/example.txt",'w') as f:
#     f.write(a)
#     f.close()

## Write a file(without overwriting)
with open(r"C:/Users/legion/Desktop/PythonFullCourse/Files/example.txt",'a') as f:
    f.write(a)
    # f.close

### Writing list of lines to a file
lines = ['First line \n','Second line\n','Third line\n']
with open(r"C:/Users/legion/Desktop/PythonFullCourse/Files/example.txt",'a') as f:
    f.writelines(lines)

### Writing Binary Files
data = b'\x00\x01\x02\x03\x04'
with open(r"C:/Users/legion/Desktop/PythonFullCourse/Files/exmaple.bin",'wb') as file:
    file.write(data)
