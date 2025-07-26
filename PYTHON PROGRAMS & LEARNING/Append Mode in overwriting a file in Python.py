# Append Mode in overwriting a file in Python

file=open("c:/Laps/Lappy.txt","a")    # append mode(a)
file.write("Working Hard Bro...")   # opens the file and overwrites
file.close()   # closing here as we use the same obj again 
file=open("c:/Laps/Lappy.txt","r")
for reading in file:
    print(reading)
    
print("\n")
print("------------------------------------")    

try:
    file=open("c:/Laps/Lappy.txt","a")
    file.write("This is MD of Lappy from PTKP")
    file.close()
    file=open("c:/Laps/Lappy.txt","r")
    for reading in file:
        print(reading)
except FileNotFoundError:
    print("File Not Found Bro...")
else:
    file.close()        