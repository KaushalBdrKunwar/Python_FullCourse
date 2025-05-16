import os

# Get and print current working directory
cwd = os.getcwd()
print(f"Current working directory is {cwd}")

# Create a new directory safely
new_directory = "pack"

if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Directory '{new_directory}' created.")
else:
    print(f"Directory '{new_directory}' already exists.")

# List files and directories
items = os.listdir('.')
print("Contents of the directory:", items)

### Joining paths
dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(dir_name,file_name)
print(full_path)
