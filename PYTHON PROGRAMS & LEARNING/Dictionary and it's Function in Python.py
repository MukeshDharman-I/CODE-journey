# Dictionary and it's Function in Python
'''
using curly brackets
based on keys and pair values
'''
user={
      "name":"MUKESH",
      "age":17,
      "job":"DATA SCIENTIST"
      }
print(user)
print(type(user))
print(user["name"])
print(user.get('age'))   # get function
print(user["age"])
print(user.keys())
print(user.values())
print(user.items())
# printing in a For Loop
for x in user:
    print(x)                 #keys will only be printed
    print(user[x])
    print("\n")
for x in user.values():
    print(x)
    print("\n")
for x in user.keys():
    print(x)
    print("\n")
for x,y in user.items():    
    print(x,y)
    print("\n")
if "age" in user:
    print("PRESENT") 
else:
    print("not present")
# Changing values
user.update({"Gender":"Male"})    
print(user)
print("\n")
user["age"]=16
print(user)
print("\n")
#popping particular index
user.pop("age")
print(user)
print("\n")
# using clear function
user.clear()
print(user)
print("\n")
# Nested dict
'''
            not working .... must know this one's function and syntax
          '''
          