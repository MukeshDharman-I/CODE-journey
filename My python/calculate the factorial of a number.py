# calculate the factorial of a number
def FACTORIAL():
    num=int(input("enter the number to find its factorial : "))
    factorial=1
    if num<0:
        print("Factorial can\'t be done if the number is NEGATIVE...")
    elif num==0:
        print("factorial the number is 1")
    else :
        for i in range(1,num+1): # if (0,num) factorial will always be zero 
            factorial*=i
        print("FACTORIAL of ",num,",",num,"! : ",factorial)
FACTORIAL()        