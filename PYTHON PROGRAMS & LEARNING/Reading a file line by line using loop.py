# Reading a file line by line using loop

file=open("c:/Laps/Lappy.txt","r")
for line in file :        # getting line by line from the obj line
    print(line)           # can directly print using variable line
    
print("\n")
print("--------------------")    

try:
    file=open("c:/L/Lappy.txt","r")
    for line in file :
        print(line)
except FileNotFoundError:
    print("File Not Found Bruh....")
else:
    file.close()        