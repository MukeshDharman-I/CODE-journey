lst=[]
limit=int(input("Enter limit : "))
for i in range(limit):
    x=int(input("Enter the value to be added : "))
    lst.append(x)
def eo():
    global lst
    odd=[]
    even=[]
    for j in lst:
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)
    
    print("ODD : ",odd,"\n","EVEN : ",even)
eo()    



    
