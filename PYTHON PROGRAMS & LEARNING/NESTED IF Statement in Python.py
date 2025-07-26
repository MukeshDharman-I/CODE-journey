# NESTED IF Statement in Python
'''
3 marks as input
Total
Average
Result
If pass Grade
   90-100  A
   80-89   B
   70-79   C
   Else    D
'''
m1=int(input("Enter mark 1 : "))
m2=int(input("Enter mark 2 : "))
m3=int(input("Enter mark 3 : "))
total=m1+m2+m3
average=total/3.0
print("Total : ",total)
print("Average : ",average)
if m1>=35 and m2>=35 and m3>=35:
    print("RESULT : PASS...")
    print("GRADE : D")
    if average>=90 and average<=100:
        print("GRADE : A")
    elif average>=80 and average<=89:
        print("GRADE : B")  
    elif average>=70 and average<=79:
        print("GRADE : C")    
        
else:
    print("RESULT : FAILED...")   
    print("NO GRADE")