'''Type casting in python '''

''' EXAMPLE 1... '''

a=10
print(a)
print(type(a))
b='hi bro'
print(b)
print(type(b))
#type casting explanations and examples below...
'''EXAMPLE 2... '''
print("\n")
print("------------------------------------------------")
print("\n")
'''here in this type of program a and b will be in string type , if we add 
   two numbers it will just join, will not add . if we want to add or multiply
   with the data type you want , just follow this programs and notes'''
   
a=input("ENTER a value of A: ")
b=input("ENTER a value of B: ")
c=a + b
print(c)
print("..................")
''' if you want to add or subtract with the data type 
you want but not join a and b as string follow this program'''
#you can use whatever the data type you want in the place of float

a=float(input("VAlue of A : "))
b=float(input("Value of B : "))
c=a+b
print(c)

print("-----------------------------------------------------")
''' how to add a integer value and a string vale '''
# actually we can,t but we can ... just follow this program
a=float(input("VAlue of A : "))
b=float(input("Value of B : "))
c=a+b
print("total :"+str(c))
#actually we can't add but a string can be added as a string
#if we didn't use'str()' we cannot add a integer or float with a string
#we have changed the integer value into string value



