#shuffle 52 cards and equally share with the given players.
import random
cards=['AceH','AceS','AceD','AceC','jackH','JackD','jackS','jackC','KingH','KingD','KingC','KingS','QueenH','QueenS','QueenD','QueenC','2H','3H','4H','5H','6H','7H','8H','9H','10H','2D','3D','4D','5D','6D','7D','8D','9D','10D','2C','3C','4C','5C','6C','7C','8C','9C','10C','2S','3S','4S','5S','6S','7S','8S','9S','10S']
random.shuffle(cards)
n=int(input("Number of players(minimum 2) : "))
N=len(cards)//n
print("Note : ",len(cards)-(N*n)," cards are removed...")
print("----------------------------------------------------")
x=1
y=1
empty=[]
for i in cards:
    empty.append(i)
    if len(empty) == (y * N):
        print(i)
        print("\n")
        print("player", x,"(Above seen)")
        print("\n")
        print("=============================================================")
        y += 1
        x += 1
    else:
        print(i)