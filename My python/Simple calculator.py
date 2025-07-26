# Simple calculator
print('''      Enter 1 for addition...
      Enter 2 for Subtraction...
      Enter 3 for Multiplication...
      Enter 4 for Division...''')
n=int(input('Enter:'))
a=int(input("Value 1:"))
b=int(input("Value 2:"))
if n==1:
    print(a+b) 
elif n==2:
    print(a-b)
elif n==3:
    print(a*b)
elif n==4:     
    print(a/b)
else:
    print("wrong number...")