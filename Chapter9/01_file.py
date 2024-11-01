# A file is data stored in a storage device. A python program can
# talk to the file by reading content from it and writing content to it.

# Types of Files.

f = f = open("C:/Users/legion/Desktop/PythonFullCourse/Chapter9/file.txt")
  # Open the file and assign it to 'f'
data = f.read()       # Read the content of the file
print(data)           # Print the content
f.close()             # Close the file
