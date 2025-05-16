#### Read the content from a source text file and write to a destination text file.
with open(r"C:/Users/legion/Desktop/PythonFullCourse/Files/example.txt") as source_file:
    content = source_file.read()

# with open(r"C:/Users/legion/Desktop/PythonFullCourse/Files/destination.txt","w") as destination_file:
#     destination_file.write(content)

### Writing then reading the file

with open(r"C:/Users/legion/Desktop/PythonFullCourse/Files/destination.txt",'w+') as destination_file:
    destination_file.write("Hellow world\n")
    destination_file.write("This is a new line \n")

    #move the file cursor to the beginning
    destination_file.seek(0)

    ## read the content of the file
    cont = destination_file.read()
    print(cont)
