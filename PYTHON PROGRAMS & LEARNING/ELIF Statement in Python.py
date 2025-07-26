# ELIF Statement in Python
'''

program in returning a book back to the library according to the data given below...

0 days late      no fine
1-5 days late    0.5 rs fine
1-10 days late   1 rs fine
10-30 days late  5 rs fine
>30 days late    Membership canceled
'''
days=int(input("enter the days : "))
if days==0:
    print("GOOD...no fine")
elif days>=1 and days<=5:
    print("NOT GOOD...0.5rs fine") 
elif days>5 and days<=10:
    print("BAD...1rs fine")
elif days>10 and days<=30:
    print("VERY BAD...5rs fine")
else:
    print("MEMBERSHIP CANCELLED...")    
    