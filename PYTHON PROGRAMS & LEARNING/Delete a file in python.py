# Delete a file in python
'''
to delete a file we have to import the os 
'''
import os

if os.path.exists("c:/delete/Delete.txt"):  # checking does the current path has the input file
    os.remove("c:/delete/Delete.txt")
else:
    print("File Not Found...")    