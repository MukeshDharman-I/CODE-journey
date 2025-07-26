# LIST in Python

'''
Sequence in Python
Mutable

a[5]
a={1,2,3,4,5}
a[0]=1
a[1]=2
a[2]=3
a[3]=4
a[4]=5
'''
a=[1,2,3,4,5]
print(a)
print(type(a))             # list type
a[0]=976
print(a)
print("SLICING...")
print(a[2])
print(a[1])
print(a[-4])
print(a[0:3])
print(a[2:])
print(a[:3])

print("-----------------------------------------")
a=[1,2.4,'ram',True,[2.3,2,False]]
print(a)
print(type(a))
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))          #boolean value (0 or 1)
print(type(a[4]))

print("-----------------------------------------------")

b=[1,1.34,True,'ramu']
print(b)
b.clear()                  #cleares the value and makes it empty
print(b)

print("-----------------------------------------------")

c=[1,4.5,'harri']
d=['True',22,555.65]
d=c.copy()                 #switches the value from one to another
print(c)
print(d)

print("---------------------------------------------")

y=[1,43,55,6,78,906]
print(y)
z=[55,89.7,'turtle',True]
print(z)
print(z.count(1))                  # finds how many times the value is there
print(z.index('turtle'))           # finds in which index the value is
print(len(z))                      # finds how many elements are there in the list
print(max(y))                  # finds which value is the maximum not applicable for str and float
print(min(y))               # finds the minimum value of the lis not applicable for str and float values

print("----------------------------------------------")

x=[10,30,54,66]
print(x)
x.pop(0)                   #removes elements using index value

print("-------------------------------------------------")

print(x) 
x=[45,78,99,8,999]
x.remove(x[2])
print(x)

print("--------------------------------------------")

l=["apple","orange","kiwi"]
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.sort(key=len)
print(l)