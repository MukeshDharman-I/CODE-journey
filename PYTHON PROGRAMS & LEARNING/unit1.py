word=input("Enter : ")
junk=""
z=True
while z:
    if word!=junk:
        for i in range(len(word)-1,-1,-1):
            junk+=(word[i])
    else:
        try:
            print("PALINDRONE")
            z=False
        except:
            print("error")