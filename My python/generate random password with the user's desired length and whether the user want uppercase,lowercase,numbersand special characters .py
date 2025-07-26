import random
length=int(input("Length of the Password : "))
password=""
upl=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowl=[]
for j in upl:
    lowl.append(j.lower())
schar=["!","@","#","$","%","^","&","*","+","~","`","/","?","/","|"]
num=["0","1","2","3","4","5","6","7","8","9"]
print("ANSWER Yes or No for the given QUESTIONS...")
a=input("\t Do you want Capital letters:").lower()
b=input("\t Do you want Small letters:").lower()
c=input("\t Do you want Numbers:").lower()
d=input("\t Do you want Special Characters:").lower()
for i in range(0,length):
    if a=="yes" and b=="yes" and c=="yes" and d=="yes":
        A = list(map(random.choice,[upl,lowl,num,schar]))
        for K in A:
            password+=K
    elif a=="yes" and b=="yes" and c=="yes" and d=="no":
        A = list(map(random.choice, [upl, lowl, num]))
        for K in A:
            password += K
    elif a=="yes" and b=="yes" and c=="no" and d=="yes":
        A = list(map(random.choice, [upl, lowl, schar]))
        for K in A:
            password += K
    elif a=="yes" and b=="no" and c=="yes" and d=="yes":
        A = list(map(random.choice, [upl, num, schar]))
        for K in A:
            password += K
    elif a=="no" and b=="yes" and c=="yes" and d=="yes":
        A = list(map(random.choice, [lowl, num, schar]))
        for K in A:
            password += K
    elif a=='yes' and b=='yes' and c=='no' and d=='no':
        A = list(map(random.choice, [upl, lowl]))
        for K in A:
            password += K
    elif a=='yes' and b=='no' and c=='no' and d=='no':
        A = list(map(random.choice, [upl]))
        for K in A:
            password += K
    elif a=='no' and b=='yes' and c=='yes' and d=='no':
        A = list(map(random.choice, [lowl, num]))
        for K in A:
            password += K
    elif a=='yes' and b=='no' and c=='yes' and d=='no':
        A = list(map(random.choice, [upl,num]))
        for K in A:
            password += K
    elif a=='no' and b=='no' and c=='no' and d=='yes':
        A = list(map(random.choice, [schar]))
        for K in A:
            password += K
    elif a=='yes' and b=='no' and c=='no' and d=='yes':
        A = list(map(random.choice, [upl,schar]))
        for K in A:
            password += K
    elif a=='no' and b=='no' and c=='yes' and d=='yes':
        A = list(map(random.choice, [num, schar]))
        for K in A:
            password += K
    elif a=='no' and b=='yes' and c=='no' and d=='yes':
        A = list(map(random.choice, [lowl,schar]))
        for K in A:
            password += K
    elif a=='no' and b=='no' and c=='yes' and d=='no':
        A = list(map(random.choice, [num]))
        for K in A:
            password += K
    elif a=='no' and b=='yes' and c=='no' and d=='no':
        A = list(map(random.choice, [lowl]))
        for K in A:
            password += K
    else:
        print("I CAN't MAKE YOU A PASSWORD....")
pas=[]
for x in password:
    if x==password[length]:
        break
    pas.append(x)
P=""
for m in pas:
    P+=m
print("PASSWORD : ",P)
print("It may cause some error")
