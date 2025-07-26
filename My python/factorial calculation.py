#factorial calculation
number=int(input("factorial number:"))
k=1
if number==1:
    print("Factorial :",number)
elif number>1:
    for i in range(1,number+1):
        k*=i
    print("factorial :",k) 
else:
    print("zero or negative can't be factorized...")    