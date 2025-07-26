# finding the sum of prime numbers
prime=[]
n=int(input("limit of numbers to sum prime numbers :"))
for i in range(2,n+1):
    x,y=2,0
    while x<=i/2:
        if i%x==0:
            y=1
        x+=1
    if y==0:
        prime.append(i)
print("prime numbers :",prime)
print("SUM : ",sum(prime))

        
    