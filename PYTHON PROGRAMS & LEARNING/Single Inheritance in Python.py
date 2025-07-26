# Single Inheritance in Python
class Nokia():
    company="Nokia India"
    website="www.nokia-india.com"
    
    def contact_details(self):
        print("Address:cherry road,near Ethamozhi,PTKP,KK")
        
class Nokiaz23(Nokia):        # derived class as it contains the base class name inside it's paranthesis
    def __init__(self):
        self.name="Nokia z23"
        self.year=1998
        
    def product_details(self):
        print("Name    : ",self.name)
        print("Year    : ",self.year)
        print("Company : ",self.company)
        print("Website : ",self.website)
        
object=Nokiaz23()
object.product_details()
object.contact_details()