one=1
while one:
    print("Create Your Account")
    username=input("Input Username : ")
    password=input("Input password : ")
    print("user \'{}\' Created Successfully...".format(username))
    one=0
print("Login Now")
two=1
while two:
    name=input("Enter Your Username : ")
    pas=input("Enter Your Password : ")
    if name!=username:
        print("Inalid user...")
    elif pas!=password:
        print("Invalid Password...")
    else:
        print("{} Successfully logged in.".format(name))
    two=0


