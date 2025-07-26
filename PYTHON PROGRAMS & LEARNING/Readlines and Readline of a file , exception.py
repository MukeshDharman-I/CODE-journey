# readlines and readline of a file , exception
try:
    file=open("c:/Laps/Lay.txt","r")   # wrong location
    print(file.readlines())
except FileNotFoundError:
    print("File not found bro...")
else:
    file.close() 
    
print("\n")
print("-----------------------------")

file=open("c:/Laps/Lappy.txt","r")
print(file.readlines(1))
print(file.readlines(2))
print(file.readlines(3))

print("\n")
print("-----------------------------")

file=open("c:/Laps/Lappy.txt","r")
print(file.read())

print("\n")
print("-----------------------------")

file=open("c:/Laps/Lappy.txt","r")
print(file.readline(4))           # reading the 4 character
print(file.readline(34))           # reading the 14 character
    