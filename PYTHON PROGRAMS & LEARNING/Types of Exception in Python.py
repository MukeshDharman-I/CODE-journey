# Types of Exception in Python

# Handiling multiple exceptions in python

print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

# name error exception
try:
    print(a)
except Exception as e:
    print(e)
    
print('OR')
      
try:
    print(a)
except NameError as e:
    print("A is not defined")      
    
print("-----------------------------------------------")

#zero divisible error

try:
    print(10/0)
except ZeroDivisionError as e:
    print("Denominator can't be zero")   
    
print("---------------------------------------------------")

# Value Error    
try:
    a=int("Lappy")   
except ValueError:
    print("Please enter numbers only")
    
print("--------------------------------------------------")    

#Index error

try:
    a=[1,2,3,4,5]
    print(a[1])
except IndexError as q:
    print("Invalid index")
    
try:
    a=[1,2,3,4,5]
    print(a[10])
except IndexError as q:
    print("Invalid index")

print("-------------------------------------------------")

#

try:
    f=open("test.txt")
except FileNotFoundError as q:
    print("File not found")
else:
    print(f.read)    

print("-------------------------------------------------")
print("-------------------------------------------------")

# Handiling Multiple exceptiuons

try:
    a=10/20
    print(a)
    b=[12,32,43,21]
    print(b[23])
except ZeroDivisionError :
    print("denominator can't be zero")
except IndexError :
    print("invalid index")
    





    

























