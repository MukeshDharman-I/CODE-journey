# Static Method in Python
class student():
    def __init__(self,Name,Gender):
        self.Name=Name
        self.Gender=Gender
    def details(self):      # self must be used or get error
        print("Name : ",self.Name," Gender : ",self.Gender)
    @staticmethod    
    def welcome():      #Staticmethod is used to avoid self
        print("Welcome to Our Institution")# This function is to show welcome to all who join our Institution
s1=student("Lappy", "male")
s1.details()
s1.welcome()        
print("----------------------------")
s2=student("Rudra", "male")
s2.details()
s2.welcome()
print("-----------------------------")      
s3=student("Zap", "male")
s3.details()
s3.welcome()          
print("-----------------------------")