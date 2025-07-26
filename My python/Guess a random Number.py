import random
rand=random.randint(1, 100)
i=1
while i<=10:
    try:
        guess=int(input("enter the Number you guessed:"))
    except NameError:
        print("Something Went Wrong...")
    if guess<rand:
        print('Your guess is too  low')
    elif guess>rand:
        print("Your guess is too hIGH")
    else:
        print("You won...")   
        break
    if i==10:
        print("Better luck next Time...")        
    i+=1    
 