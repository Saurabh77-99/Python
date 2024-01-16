# copyfile = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt','copy.txt') #src,dst
# shutil.copyfile('test.txt','c:\\Users\\Desktop\\folder\\direct\\copy.txt') #src,dst 
# you can add location of file too

# shutil.copy('test.txt','copy.txt') #src,dst
# shutil.copy2('test.txt','copy.txt') #src,dst