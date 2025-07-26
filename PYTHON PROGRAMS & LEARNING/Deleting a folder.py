# Deleting a folder 

import os

if os.path.exists("c:/delete/Delete.txt"):  # checking does the current path has the input file
    os.remove("c:/delete/Delete.txt")
    #os.rmdir("delete")................this comment can delete the folder , folder name is must, EG:delete
else:
    print("File Not Found...")    