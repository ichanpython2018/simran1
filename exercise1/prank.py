import os
from string import *
list_files=os.listdir("C:\\Users\\test\\Downloads\\prank")
print(list_files)
os.chdir("C:\\Users\\test\\Downloads\\prank")
for file in list_files:
    #get oldname of file
    oldname=file
    print(oldname)
    #newname of file=oldname-numbers
    #newname=oldname.lstrip(digits)
    newname=oldname.lstrip(punctuation)
    #list_files=list_files.replace(character, "")
    print(newname)
    #rename the file
    os.rename(oldname,newname)