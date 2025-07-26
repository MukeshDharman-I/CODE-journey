import random
class Game:
    com=random.randint(1, 10)  # numbers from 1 to 10
    guess=int(input("Guess a num  (1-10):"))
    chance=0
    i=0
    def process(self):
        while Game.i<=10:
            if Game.guess==Game.com:
                print("Won!")
                break
            else:
                Game.chance+=1
                if Game.chance==9:
                    print("Last Chance...")
                elif Game.chance==10:
                    break
                else:
                    print("Try again...")
                    Game.guess=int(input("Guess again:"))
            Game.i+=1   
P=Game()
print(P.process())
    