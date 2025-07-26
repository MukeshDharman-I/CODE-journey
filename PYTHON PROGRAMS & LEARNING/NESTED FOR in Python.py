# NESTED FOR in Python
'''

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

for i in range(6):
    for j in range(i):       # this line is explained in note
        print("*",end="")    #'end="' makes the star to be printed near by near
    print("")                #new line
    
    
print("---------------------------------")    
    
for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("")
    
print("---------------------------------")    
        
for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")  