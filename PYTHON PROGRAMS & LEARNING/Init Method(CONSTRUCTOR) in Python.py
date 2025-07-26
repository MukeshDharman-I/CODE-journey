# Init Method(CONSTRUCTOR) in Python
'''
we don't call as constructor in python as we call it as init 
'''
class user():
    def __init__(self,name):    # instead of self we can use anything
        print("call when new instance is created")
        self.name=name
    def printall(self):
            print("Name :",self.name)
o=user("MukeshDharman")
o.printall()
print(o.__dict__)
print("========================================")
o1=user("Lappy")
o1.name
print(o1.__dict__)                              # stored as instance attribute
print("========================================")
        