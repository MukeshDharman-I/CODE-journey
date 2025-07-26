a=int(input("Enter a Number : "))
lst=[]
if a<2:
    print("Not a prime number")
elif a==2:
    print("nor prime nor composite")
else:
    for i in range(1,a+1):
        if a%i==0:
            lst.append(i)
    print(lst)
    if len(lst)==2:
        print("Prime Number")
    else:
         print("Not Prime Number")