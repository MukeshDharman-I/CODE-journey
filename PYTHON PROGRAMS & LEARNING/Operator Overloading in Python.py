# Operator Overloading in Python

'''
Every datatype is acting as class

eg for operator overloading

a=12
b=54
print(a+b)
z=("Lappy")
X=("Wins")
print(Z+W)
'''
class addition():
    
    def __init__(self,a):
        self.a=a
        
    def __add__(o1,o2):         # Must Required for addition of overlading operator
        return o1.a + o2.a
    
    def __sub__(o1,o2):         # Must Required for subtraction of overlading operator
        return o1.a - o2.a
        
o1=addition(9)
o2=addition(6)

print("Add : ",(o1 + o2))
print("Sub : ",(o1 - o2))     # we can use such for many of the magic (method) operators

