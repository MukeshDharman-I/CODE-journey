# write a program to replace inbuild replace function

ADD=''
String=input("Enter a string :")
A=input("which to change:") 
B=input("what to change:") 
for i in String:
    if i!=A:
        ADD+=i
    else:
        ADD+=B
print(ADD)        