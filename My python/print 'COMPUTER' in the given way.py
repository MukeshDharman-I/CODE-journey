# print 'COMPUTER' in the given way
'''
COMPUTER
COMPUTE
COMPUT
COMPU
COMP
COM
CO
C

&

C
CO
COM
COMP
COMPU
COMPUT
COMPUTE
COMPUTER
'''
str1=input("Enter a string :")
index=0
for j in str1:
    print(str1[:index+1])
    index+=1
print("-------------------------------------")
str = input("Enter the string :")
index=len(str)
for i in str:
    print(str[:index])
    index-=1