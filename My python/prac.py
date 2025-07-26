class Restaurant():
    def __init__(self,name,dish):
        self.name=name
        self.dish=dish
    def ps(self):
        print(f"Restaurant is open")  
        print(f"{self.name} is here with your {self.dish}")
class IceCreamStand(Restaurant):
    def __init__(self, name, dish,*lst):
        super().__init__(name, dish)
        self.lst=list(lst)
    def flavour(self):
        print(f"flavours available are {self.lst}")
class Admin():
    def __init__(self):
        self.storage=["can add post", "can delete post", "can ban user"]
        self.p=privilage() 
    def privilages(self):
        print(f"Privilages are {self.storage}") 
class privilage():
    def __init__(self):
        self.priv=["can add post", "can delete post", "can ban use"]   
    def privilag(self):
        print(f"Privilages are {self.priv}")                 
flav=input("Enter those flavours :").split(",")        
ice=IceCreamStand("happy_mood","pizza",*flav)   
ice.ps()
ice.flavour()
ad=Admin()
ad.privilages()
ad.p.privilag()
