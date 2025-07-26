print('''
      1 for multiplication
      2 for addition 
      3 for suntraction
      4 for quotient
      5 for reminder
      6 for the calculation of more than two numbers
      7 for exit''')
num = int(input("enter the Number choosed:"))
if num==1:
    a=int(input("entter num 1 :"))
    b=int(input("enter num 2:"))
    print(a*b)
elif num==2:
    a=int(input("entter num 1 :"))
    b=int(input("enter num 2:"))
    print(a+b)
elif num==3:
    a=int(input("entter num 1 :"))
    b=int(input("enter num 2:"))
    print(a-b)
elif num==4:
    a=int(input("entter num 1 :"))
    b=int(input("enter num 2:"))
    print(a/b)
elif num==5:
    a=int(input("entter num 1 :"))
    b=int(input("enter num 2:"))
    print(a%b)
elif num==6:
    print('''
          use * for multiplication
          use + for addition
          use - for subreaction
          use / for division
          use % for reminder
          ''')
    Z=input("type your expression:")
    print(eval(Z))
elif num==7:  
    print("Miss you")
    print("hope you will come back")
else:
    print("I think  you have given the wrong number...")
    num=int(input("enter the number you choosed:"))
