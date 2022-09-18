 # ROCK PAPER SCISSOR GAME

import random

def gameWinner(Computer, Player):
    if Computer == Player:
        return None
    elif Computer == "r":
        if Player == "p":
           return True
        elif Player == "s":
            return False
    elif Computer == "p":
        if Player == "r":
            return False
        elif Player == "s":
            return True
    elif Computer == "s":
        if Player == "r":
            return True
        elif Player == "p":
            return False

print ("Computer Turn : Rock(r) Paper(p) scissor(s)") 
randomNo = random.randint(1,3)
if randomNo == 1:
    Computer = "r"
elif randomNo == 2:
    Computer = "p"
elif randomNo == 3:
    Computer = "s"
Player = input("Player's Turn : Rock(r) Paper(p) Scissor(s) : ")

print (f"Computer Chose : {Computer}")
print (f"You Chose : {Player}")

a = gameWinner(Computer, Player) 

if a:
    print( "You WIN!")
elif a==None:
    print("GAME tie!")
else:
    print("Game Lose!")


