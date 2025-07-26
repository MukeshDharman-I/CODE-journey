# Property Decorator in Python
class user():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # self.msg=self.name +" is "+ str(self.age ) + " year old"
    @property            # msg will be converted to a property
    def msg(self):                                        # property decorator is used 
            return self.name +" is "+ str(self.age ) + " year old"
o=user("Lappy", 17)   
print(o.name)
print(o.age)
print(o.msg)          # as msg is a function now not an attribute add an paranthesis but as we use property we don't want to use paranthesis
o.age=16                  # to change the value of age in msg we are,            
print(o.age)              # Going to use property decorator (in up)
print(o.msg)
