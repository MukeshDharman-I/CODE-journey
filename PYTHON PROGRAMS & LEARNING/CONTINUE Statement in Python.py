# CONTINUE Statement in Python
'''
print all odd numbers from 1 to 20 using continue statement
'''

i=1
while i<=20:
    if i%2==0:
        i+=1
        continue; # the if statement checks whether the num is even and if the num is even using continue statement it skips the even number and increments the num and executes which is the odd num
    print(i)
    i+=1