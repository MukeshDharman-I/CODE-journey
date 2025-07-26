# Set in Python
'''
using curly brackets 
like tuple and list but not so
'''
names={'smart work','work hard','concentrate'}
print(names)
print(type(names))
print("\n")
# Access Values Using For Loop
for name in names:
    print(names)
print("\n")
# Adding New Elenment    
names.add('sharja')
print(names)
print("\n")
# Update Another Set of Data
a={'care','enjoy','move on'}
names.update(a)
print(names)
print("\n")
# Removing A Data
names.remove('sharja')
print(names)
print("\n")
# Discarding An Item......................if the item is there it will remove if not it will leave
names.discard('enjoy')
print(names)
print("\n")
# Using Pop Function...............removes a random value
names.pop()
print(names)
print("\n")
# Using Clear Function
names.clear()
print(names)
print("\n")
# deleting names
del names
print("\n")
# Removes dulplicate values automatically
v={'smart work','work hard','concentrate','work hard'}
print(v)
print("\n")
print("-----------------------------------------------------")
print("\n")
# Union Function
a={1,2,3,4,5}
b={'a','b','c','d'}
c=a.union(b)
print(c)
print("\n")
# Update Function
a.update(b)
print(a)
print("\n")
# Intersection Function
a={1,3,2,4,5}
b={'a','v','j',1,4}
c=a.intersection(b)
print(c)
print("\n")
# Symmetric Difference
a={1,3,2,4,5}
b={'a','v','j',1,4}
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)
print("\n")
# Is Disjoint Function
x={3,2,5}
y={'a','v','j'}  # no similar values so it is aTRUE
z=x.isdisjoint(y)
print(z)
print("\n")
# Is Subset Function
z=x.issubset(y) 
print(z)
print("\n")
# Finding is it a superset
z=y.issubset(x)
print(z)        # if each value in both sets are equal it shows true
print("\n")
print("--------------------------------------------------------")





































































































