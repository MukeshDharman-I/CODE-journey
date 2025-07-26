from bird import *
class one(bird):
    def __init__(self):
        '''nothing to say'''
    def o(self):
        print(self.name*2)
        print(self.count)
k=one()
k.out("gopal")
k.o()
k=one()
print(one.__doc__)
k.out("Sutha")
k.o()