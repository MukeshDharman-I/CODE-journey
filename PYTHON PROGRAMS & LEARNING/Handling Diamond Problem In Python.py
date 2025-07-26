# Handling Diamond Problem In Python

class A():
    
    def display(self):
        print("I am the display of class A...")
        
class B(A):
     
    def display(self):
        print("I am the display of class B...")

class C(A):        
    
    def display(self):
        print("I am the display of class C...")
        
class D(B,C):        
    
    def display(self):
        print("I am the display of class D...")        
        
o=D()
o.display()        

print("\n")
print("--------------------------------------------------")
print("\n")

class A():
    
    def display(self):
        print("I am the display of class A...")
        
class B(A):
     
    pass

class C(A):        
    
    pass
        
class D(B,C): # it first checks D and checks it's inherited class thus, acts in a sequence
    
    pass
        
o=D()
o.display()
        