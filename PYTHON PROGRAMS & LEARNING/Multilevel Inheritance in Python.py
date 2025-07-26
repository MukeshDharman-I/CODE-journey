# Multilevel Inheritance in Python

class Grandfather():
    
    def own_house(self):
        print("Grandpa House")
        
class Father(Grandfather):
    
    def own_bike(self):
        print("Father's Bike")    

class Son(Father):    # can access the data of father and grandfather and it's own
    
    def own_car(self):
        print("Son Have A Car")
o=Son()
o.own_car()
o.own_house()
o.own_bike()
        