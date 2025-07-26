# find the greatest digit of four numbers
def Finding_greatest():
    a=int(input("Enter Number 1 : "))
    b=int(input("Enter Number 2 : "))
    c=int(input("Enter Number 3 : "))
    d=int(input("Enter Number 4 : "))
    if a>b and a>c and a>d :
        print("A is greater...")
    elif b>a and b>c and b>d :
        print("B is Greater...")
    elif c>a and c>b and c>d :
        print("C is Greater...")
    else :
        print("D is Greater...")    
Finding_greatest()