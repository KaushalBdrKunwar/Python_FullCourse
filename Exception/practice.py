# File Handling and Exception Handling

try:
    file = open('hero.txt', 'r')
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File does not exist.")

finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print('File closed.')
