# TUPLE in Python
                 #...Immutable
                 #...sourrended by round brackets(1,2,3)
                 
a=(22,"turkey",True,4.6)
print(a)
print(type(a))
print(a[1])
print(a[-1])                 # Negative index
print(a[0:2])
b=list(a)                #changed tuple into list as tuple is immutable(can,t change the values)
print(b)
b.append("Raja")
print(type(b))
a=tuple(b)
print(a)
print(type(a))        #changed list into tuple
print("\n")
for i in a :
    print(i)
print("\n")
if "turkey" in a:
    print("Turkey is found")
else:
    print("Not found")
print("\n")
print(len(a))
print("\n")
a=(1)
print(type(a))        # why it's type is an int ? solution in nxt line
print("\n")
a=(1,)
print(type(a))     #use a comma if u have single value inside the paranthesis
print("\n")
#we can't remove an element in tuple  like list but we can delete
del a
a=(1,2,3,4,5)
b=(5,6,7,8)
c=a+b         #it's not an addition . it is concadination
print(c)
print("\n")
print(c.count(5))  # counts what item we choose
# creating nested tuple
print("\n")
a=(12,34,56,78)
b=(98,76,54,32)
c=(a,b)
print(c)
print(c[0])
print(c[1])
print("\n")
x=("MUKESH",)*4
print(x)
print("\n")
a=(1,2,3,4,5,6,7)
print(min(a))
print(max(a))
























    