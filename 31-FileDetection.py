import os

path = "C:\\Users\\HP\\OneDrive\\Desktop\\Filepy.txt" # -> File
# path = "C:\\Users\\HP\\OneDrive\\Desktop\\Python" #->Folder

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a File")
    elif os.path.isdir(path):
        print("That is Directory")
else:
    print("That location doesn't exists")