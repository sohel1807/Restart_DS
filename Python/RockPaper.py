import random
while True:
    choices=["rock","paper","scissors"]

    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock,paper or scissors?:").lower()
    if player==computer:
        print("player:",player)
        print("computer:",computer)
        print("Tie!!")
    elif player=='rock':
        if computer=='paper':
            print("player:",player)
            print("computer:",computer)
            print("You loose!!")
        if computer=='scissors':
            print("player:",player)
            print("computer:",computer)
            print("You Win!!")
    elif player=='scissors':
        if computer=='rock':
            print("player:",player)
            print("computer:",computer)
            print("You loose!!")
        if computer=='paper':
            print("player:",player)
            print("computer:",computer)
            print("You Win!!")
    elif player=='paper':
        if computer=='scissors':
            print("player:",player)
            print("computer:",computer)
            print("You loose!!")
        if computer=='rock':
            print("player:",player)
            print("computer:",computer)
            print("You Win!!")

    play_again=input("play again (yes/no)?:").lower()

    if play_again!="yes":
        break

print("bye!!!")

    


