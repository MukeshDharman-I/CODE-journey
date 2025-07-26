# Multiple Inheritance in Python
class Father():
    
    def fishing(self):
        print("Fishing in Ocean")
        
    def chess(self):
        print("Playing well in chess")
        
class Mother():
    
    def Cooking(self):
        print("Cooking in Kitchen")
        
    def chess(self):
        print("Playing well in chess")
        
class Son(Father,Mother):   # This derive class can access the data of both the base class
    
    def riding(self):
        print("Good in Cycle Riding")
o=Son()
o.riding()
o.fishing()
o.chess()
o.Cooking() 
        