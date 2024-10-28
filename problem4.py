# Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

# Function to list the contents of a directory (You can change this function if needed)
def list_directory_contents(directory_path='/'):
    try:
        # This function os.listdir() retrieves the contents of the directory (You can change this method)
        contents = os.listdir(directory_path)
        
        # Printing the directory contents
        print(f"Contents of '{directory_path}':")
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for accessing the directory '{directory_path}'.")

# Test the function with a specific directory path (You can change this directory path)
list_directory_contents()  # Pass a directory path as an argument if needed

