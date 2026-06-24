import random

#create a rock paper scissor game
ch =""
game = ["rock","paper","scissor"]
while ch not in game:
    ch= input("Enter rock or paper or scissor : ").lower()


if((random.choice(game) == "rock" and ch=="rock") or (random.choice(game) == "paper" and ch=="paper") or (random.choice(game) == "scissor" and ch=="scissor")):
    print("Its a tie")
elif(random.choice(game) == "rock" and ch == "paper"):
    print("Computer : Rock Player :",ch)
    print("Player Wins")
elif(random.choice(game) == "rock" and ch == "scissor"):
    print("Computer : Rock Player :",ch)
    print("Computer Wins")
elif(random.choice(game) == "paper" and ch == "rock"):
    print("Computer : Paper Player :",ch)
    print("Computer Wins")
elif(random.choice(game) == "paper" and ch == "scissor"):
    print("Computer : paper Player :",ch)
    print("Player Wins")
elif(random.choice(game) == "scissor" and ch == "rock"):
    print("Computer : Scissor Player :",ch)
    print("Player Wins")
elif(random.choice(game) == "scissor" and ch == "paper"):
    print("Computer : Scissor Player :",ch)
    print("Computer Wins")