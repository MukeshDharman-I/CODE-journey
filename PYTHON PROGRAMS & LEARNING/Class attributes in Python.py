# Class attributes in Python

class student():
    name = "Mukeshdharman"
    age = 17                        # Name and Age are class attributes
# getattr method    
print("NAME :",getattr(student,'name'))
print("AGE :",getattr(student,'age'))
print(getattr(student,'gender','NO SUCH ATTRIBUTE FOUND')) # third one is an opptional which handles the error if there is no such attribute and etc...
# Dot Notation method
print(student.name)
print(student.age)
# Setattr
setattr(student, 'name', 'Lappy')                                        # to set a value or replace a value 
print(student.name)

setattr(student, 'gender', 'male')
print(student.gender)

student.city="Nagercoil"
print(student.city)

print("---------------------------------------------")
# class's data nd function will stored in dictionary, in the format of mapping proxy object
print(student.__dict__) 
print("---------------------------------------------")
# can use delete option to delete an attribute
delattr(student,"city")
print(getattr(student, 'city','NO SUCH ATTRIBUTE FOUND....'))
print(student.__dict__)       # city will not be found

del student.gender
print(getattr(student, 'gender','NO SUCH ATTRIBUTE FOUND...'))
print(student.__dict__)       # gender will not be found




















