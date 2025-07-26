# user Define Function in Python( all types)

'''
def - keyword
name of the function()
and a collen:

syntax:

def welcome():    
    
'''
# No Return Type Without Argument Function in Python
def welcome():
    print("welcome to Python")
welcome()    
print("-------------------------")
def add():
    a=int(input("Enter The Value Of A : "))
    b=int(input("Enter The Value Of B : "))
    c=a+b
    print("Total : ",c)
add()    
print("\n")
print("-----------------------------------------------------------")
# No Return Type With Argument Function in Python
def sub(a,b):
    c = a - b
    print("Difference : ",c)
sub(60,55)    
print("\n")
print("-----------------------------------------------------------")
# Return Type With Argument Function in Python
def mul():
    a=int(input("Enter The Value Of A : "))
    b=int(input("Enter The Value Of B : "))
    c=a*b
    return c
x=mul()
print("Product : ",x)
print("\n")
print("-----------------------------------------------------------")
# Return Type Without Argument Function in Python
def div(a,b):
    c=a/b
    return c
z=div(12, 3)
print("Quotient : ",z)            




















