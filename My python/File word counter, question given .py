''' create a program to read a txt file and
 count the occurances of each word , with and without build-in function
'''

# with build-in function
text=input("enter the text :")
srch=input("enter the character to be counted : ")
print("counts :",text.count(srch))

print("\n")
print("----------------------------------------------")
print("\n")

# Without build-in function
text=input("enter the text :")
srch=input("enter the character to be counted : ")
z=0
for i in text:
    if i==srch:
        z+=1
print("Counts:",z)        