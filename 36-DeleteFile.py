import os
import shutil

# path = "DeleteFile.txt"
path = "DeleteFolder"
# os.remove('DeleteFile.txt')
# os.remove('filepath if it was in some other locations on computer')

try:
    # os.remove(path) # -> Delete a file
    # os.rmdir(path) #-> delete an empty folder 
    shutil.rmtree(path) # delete folder containing all files
except FileNotFoundError:
    print("The file was not found")
except PermissionError: # for folder permission access!
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete using that function")
else:
    print(path + " was deleted")
