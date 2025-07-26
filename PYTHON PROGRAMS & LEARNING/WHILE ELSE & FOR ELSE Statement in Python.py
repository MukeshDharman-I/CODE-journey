# WHILE ELSE & FOR ELSE

i=1
while i<=5:
     print(i)
     i+=1
else:
    print("loop completed")   # if the loop successfully completed else statement will execute
    
print("----------------------------------")

for i in range(1,11):
    print(i)
else:
    print("for loop completed")

#if loop did,nt completed

print("----------------------------------") 

for i in range(1,11):
    if i==5:
        break
    print(i)
else:
    print("for loop completed")

#if loop did,nt completed   