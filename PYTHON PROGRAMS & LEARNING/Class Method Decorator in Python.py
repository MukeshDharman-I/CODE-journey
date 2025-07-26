# Class Method Decorator in Python
class student():
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count+=1
    def printdetails(self):
        print("name : ",self.name ,"Age : ",self.age)
    @classmethod    
    def total(cls):
        return cls .count
o=student("lappy", 17)
o.printdetails()
print("Total Admission : ",student.total())
o=student("Rudra",16)
o.printdetails()
print("Total Admission : ",student.total())
o=student("Thandav",15)
o.printdetails()
print("Total Admission : ",student.total())