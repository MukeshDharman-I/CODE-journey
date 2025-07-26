# Function Overriding in Python
'''
a class is derived from a class and if the derived class use the function of same name of 
the base class it is function overriding 
'''
class employee():
    
    def workinghours(self):
        self.hrs=50
        
    def printhours(self):
        print("Total Working Hours : ",self.hrs)
        
class trainee(employee):
    
    def workinghours(self):
        self.hrs=60
        
    def printhours(self):
        print("Total Working Hours : ",self.hrs)     # trainee finished his training & it's time upgrade his timing
        
    def reset_working_hours(self):
        super().workinghours()            # use super() function to access the data of the base class's function eventhough the function of derived class is with the same name 
             
    def reset_print_hours(self):
        super().printhours()
        
e=employee()
e.workinghours()
e.printhours()        
        
t=trainee()
t.workinghours()
t.printhours()  
t.reset_working_hours()
t.reset_print_hours()      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        