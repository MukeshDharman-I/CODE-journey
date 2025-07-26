# Property Decorator Getter Setter
class student():
    def __init__(self,total):
        self._total=total          # if we use underscore infront of a variable it acts as an private variable
    def average(self):
        return self._total/6.0
    @property        # getter function
    def total(self):
        return self._total
    @total.setter    # setter function
    def total(self,t):
        self._total=t
o=student(567)    
print("Total :",o.total)        # to access a private variable we have to craete a functionlity
print("Average :",o.average())
o.total=581                        #print("Total :",o.total()) ...........TypeError: 'int' object is not callable
print("Total :",o.total)          # to sole this problem we use getter setter
print("Average :",o.average())

