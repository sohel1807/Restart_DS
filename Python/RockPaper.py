import random
Win_count=0
lose_count=0
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
            lose_count+=1
        if computer=='scissors':
            print("player:",player)
            print("computer:",computer)
            print("You Win!!")
            Win_count+=1
    elif player=='scissors':
        if computer=='rock':
            print("player:",player)
            print("computer:",computer)
            print("You loose!!")
            lose_count+=1
        if computer=='paper':
            print("player:",player)
            print("computer:",computer)
            print("You Win!!")
            Win_count+=1
    elif player=='paper':
        if computer=='scissors':
            print("player:",player)
            print("computer:",computer)
            print("You loose!!")
            lose_count+=1
        if computer=='rock':
            print("player:",player)
            print("computer:",computer)
            print("You Win!!")
            Win_count+=1

    play_again=input("play again (yes/no)?:").lower()

    if play_again!="yes":
        print(Win_count,lose_count)
        break

print("bye!!!")

    


