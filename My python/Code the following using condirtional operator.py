# code the following using conditional operator
# odd or even
#which is greater
#eligibility for vote
#leap year
'''
syntax:
    
    if-true returns-this if (test-expression) else if-false-return-this
'''
print("ODD or EVEN...")
a= int(input(" Enter NUM : "))
print("NUM is ODD..."if (a%2==1) else "NUM is EVEN...")
print("\n")
print("WHICH IS GREATER...")
a= int(input("Enter NUM 1 : "))
b= int(input("Enter Num 2 : "))
print("NUM 2 is GREATER..."if (a<b) else "NUM 1 is GREATER...")
print("\n")
print("Eligible to vote or not...")
a= int(input(" Enter your AGE : "))
print("ELIGIBLE to VOTE "if (a>=18) else "NOT ELIGIBLE TO VOTE...")
print("\n")
print("LEAP YEAR or not...")
a= int(input(" Enter the year : "))
print("It\'s a LEAP YEAR... "if (a/400==0 and a/100==0) else "It\'s NOT a LEAP YEAR......")
print("\n")

