import os

source = "Test1.txt"
destination = "C:\\Users\\HP\\OneDrive\\Desktop\\MoveFile.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source +" was found")
except FileNotFoundError:
    print(source+" was not found")
