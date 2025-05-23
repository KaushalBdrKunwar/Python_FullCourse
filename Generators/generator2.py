## Use case of generator to read large files

def read_large_file(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield line

file_path = r"C:/Users/legion/Desktop/PythonFullCourse/Generators/genfile.txt"

for line in read_large_file(file_path):
    print(line.strip())
