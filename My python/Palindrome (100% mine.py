s=input("Enter a string :")
x,y=0,len(s)-1
for i in s:
    if s[x]==s[y]:
        x+=1
        y-=1
        if x==y:
            print("Palindrome")
    else:
        print("NOT palindrome")
        break