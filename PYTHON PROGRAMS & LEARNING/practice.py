import random
class game:
    chance = 0
    i=3
    limit = 3
    rand = random.randint(1,10)
    def __init__(self):
        print("WELCOME To GAME !")
    def process(self):
        z = True
        while z:
            if game.chance != game.limit:
                game.chance += 1
                game.i -= 1
                choice = int(input("Guess the Number(1-10) : "))
                if choice == game.rand:
                    print("You WON !")
                    break
                else:
                    print(game.i , "Chance left")
                    continue
            else:
                return("You Lost!")
                z = False
game = game()
print(game.process())







