# IF ELSE statement in Python
'''
write a program to check vote eligibility by entering his/her name and age
'''
name=input("Enter your name : ")
age=int(input("Enter your age : "))
if age>=18:
    print(name,"age is",age,"Eligible for Vote")
else:
    print(name,"age is",age,"NOT Eligible for vote")