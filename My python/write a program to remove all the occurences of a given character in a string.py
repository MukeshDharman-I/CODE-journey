# write a program to remove all the occurences of a given character in a string
str=input("Enter a string : ")
ch=input("Enter the character to be removed : ")
Z=""
for i in str:
    if ch==i:
        pass
    else:
        Z+=i
print(Z)