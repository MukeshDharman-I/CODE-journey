# Instance Attribute in Python

class user():
    course='java'
o=user()                         # created new object
print(user.__dict__)
print("---------------------------------------")
print(user.course)
print(o.__dict__)                # it is empty , then it checks it's class whether it has obj course and prints
print(o.course)                  # printing course using the new obj
print("---------------------------------------")
o.course='c++'
print(o.__dict__)                # it checkes whether it has an obj if not prints obj from the class(now o has an obj c++)
print(o.course)                    
print("---------------------------------------")
o2=user()
print(o2.__dict__)
print(o2.course)                # if th instance obj does'nt have any attribute,the value you have given will be taken as it's attribute and stored in its namespace

 