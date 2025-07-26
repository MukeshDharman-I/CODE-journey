# String and string function in python

L="Mukesh Dharman"
print(L)
print(type(L))
print(L.upper()) #makes all letters capital
print(L.lower()) #makes all letter small
print(L.capitalize()) #makes the starting word capital 'M'
print(L.title()) #makes the first starting 'M' and 'D'
print(L.count("a")) #counts how many a is there
print(L.endswith("an")) #if the last letters are correct it returns true if not false
print(L.find("h"))  # finds where the first 'h' letter is 
print(L.find("h",7)) # here 7 tells that find h after the seventh letter 
print(L.replace("e", 'ku')) # replaces e as ku
a="lappy"
print("Is Upper : ",a.isupper())
print("Is Lower : ",a.islower())
print("Is Alpha Numeric : ",a.isalnum())
print("Is Alpha : ",a.isalpha())
s="Lambo\nRolex\nFerrari"
print(s)
print(s.splitlines())
print(s.splitlines(True))
g="Mukesh Dharman Is A Good Boy"
print(g.split(" "))
print(g.split(","))
i="    LAPPY  "
print(len(s))    #finds the length of with the space
print(len(s.strip()))  # finds the length by avoiding space
print(len(s.lstrip())) # finds length by avoiding the left spaces
print(len(s.rstrip())) #finds the length by avoiding the right spaces