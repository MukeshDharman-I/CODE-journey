# print "COMPUTER" in the given below form:
'''
COMPUTER
COMPUTE
COMPUT
COMPU
COMP
COM
CO
C
'''    
    
str="COMPUTER"
i=len(str)
while 0<i:
    print(str[:i])
    i-=1
print("=============================")
print("or")
print("=============================")
str="COMPUTER"
index=len(str)
for i in str:
    print(str[:index])
    index-=1    
    