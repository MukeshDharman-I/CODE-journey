# Abstract Base Class in Python
'''
creating set of rules and implementing classes under the rule
.
.
.
abc =>Abstract Base Class
.
.
.
Importing abstract base class 
'''
from abc import ABC ,abstractmethod

class Bank(ABC):  # now it is a abstract class,rule is the functions should not have defnition
    @abstractmethod        # becomes abstract method
    def loan(self):
        
        pass
        
    @abstractmethod    
    def credit(self):
        
        pass
        
    @abstractmethod    
    def debit(self):
        
        pass
    
class HDFC(Bank):  # have to redifine all the functions of bank to work
    
    def loan(self):
        print("We provide 7.5% Interest Loan")
    def credit(self):
        print("HDFC provide credit")
    def debit(self):
        print("HDFC provide debit")       
    def card(self):             # functions can be added newly
        print("HDFC provides card")

o=HDFC()
o.loan()
o.credit()
o.debit()
o.card()


























    
    