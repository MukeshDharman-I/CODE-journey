# print * and ABCDE Question
'''
another  method is inn thhe file ' NESTED FOR ' 
print:
    
*
**
***
****
*****

and

*****
****
***
**
*

and

ABCDE
ABCED
ABCDE
ABCDE
ABCDE
ABCDE

a-z => 97-122                 ACSII value
A-Z => 65-90

'''

i=1
while(i<=6):
    for j in range(1,i+1):
        print("*",end="")
    print("")
    i+=1    
    
print("")
print("-----------------------------------")
print("")

i=6
while(i>=1):
    for j in range(0,i):
        print("*",end="")
    print("")
    i-=1 
    
print("")
print("-----------------------------------")
print("")  

for i in range(6):
    for j in range(65,65+i):
        print(chr(j),end="")
    print("")
    
print("")
print("-----------------------------------")
print("")  

i=6
while(i>=1):
    for j in range(65,65+i):
        print(chr(j),end="")
    print("")
    i-=1

print("---------------------------------------")   

n=9
for i in range(1,6):
    print(("* "*i).center(n," "))   
