# Recursive Function in Python 
''' 
if the function calls itself to complete it's work is called recursive function 
'''
'''
5!(factorial)=1*2*3*4*5=120
'''
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print("factorial of 5 :",factorial(5))    
'''
x!=1 , then
=>5*factorial(5-1)
=>5*factorial(4)
=>5*4*factorial(4-1)
=>5*4*factorial(3)
=>5*4*3*factorial(3-1)
=>5*4*3*factorial(2)
=>5*4*3*2*factorial(2-1)
=>5*4*3*2*1factorial(1)
=>5*4*3*2*1=120
'''