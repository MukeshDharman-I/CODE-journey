# Write or Overwrite a File in Python
'''
going to know about write mode w 
'''

file=open("c:/Laps/Lappy.txt","w")    # write mode(w)
file.write("This is MD of Lappy from PTKP")   # opens the file and overwrites
file.close()   # closing here as we use the same obj again 
file=open("c:/Laps/Lappy.txt","r")
for reading in file:
    print(reading)
    
print("\n")
print("------------------------------------")    

try:
    file=open("c:/Laps/Lappy.txt","w")
    file.write("This is MD of Lappy from PTKP")
    file.close()
    file=open("c:/Laps/Lappy.txt","r")
    for reading in file:
        print(reading)
except FileNotFoundError:
    print("File Not Found Bro...")
else:
    file.close()        