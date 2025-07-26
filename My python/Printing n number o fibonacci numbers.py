# Printing n number of Fibonacci numbers

n = int(input("Enter the number of fionacci nummbers to be printed :"))
a=-1
b=1
for i in range(1,n+1): # or (0,n)
    c=a+b
    print(c)
    a=b
    b=c
    
print("\n")
print("-----------------------------------")

def fibonacci():
    n = int(input("Enter the number of fionacci nummbers to be printed :"))
    a=-1
    b=1
    for i in range(0,n): # or (1,n+1)
        c=a+b
        print(c)
        a=b
        b=c
fibonacci()  # or... print(Fibonacci())  
    
     