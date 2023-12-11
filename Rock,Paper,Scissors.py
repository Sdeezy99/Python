choice_1 = ""
choice_2 = ""
rematch = ""


def draw(choice1,choice2):
    if (choice1 == "R" and choice2 == "R"):
        print("It's a tie")
    elif (choice1 == "P" and choice2 == "P"):
        print("It's a tie")
    elif (choice1 == "S" and choice2 == "S"):
        print("It's a tie")


def player1(choice1,choice2):
    
    if (choice1 == "R" and choice2 == "S"):
        print("Player 1 wins")
    elif (choice1 == "P" and choice2 == "R"):
        print("Player 1 wins")
    elif (choice1 == "S" and choice2 == "P"):
        print("Player 1 wins")


def player2(choice1,choice2):
    
    if (choice1 == "R" and choice2 == "P"):
        print("Player 2 wins")
    elif (choice1 == "P" and choice2 == "S"):
        print("Player 2 wins")
    elif (choice1 == "S" and choice2 == "R"):
        print("Player 2 wins")

print("This is a Rock,Paper,Scissors game. Player 1 and 2 can choose their option to win the game")
print("Rock = R,Paper = P,Scissor= S")
print("Player one choose your choice (Rock/Paper/Scissors) or (R/P/S)")
choice_1 = input().upper()
print("Player two choose your choice (Rock/Paper/Scissors) or (R/P/S)")
choice_2 = input().upper()

draw(choice_1,choice_2)
player1(choice_1,choice_2)
player2(choice_1,choice_2)

print("Do you want a rematch? (Y/N)")
rematch = input().upper()

if (rematch == "Y"):
    while (rematch == "Y"):
        print("Player one choose your choice (Rock/Paper/Scissors) or (R/P/S)")
        choice_1 = input().upper()
        print("Player two choose your choice (Rock/Paper/Scissors) or (R/P/S)")
        choice_2 = input().upper()
        draw(choice_1,choice_2)
        player1(choice_1,choice_2)
        player2(choice_1,choice_2)
        print("Do you want a rematch? (Y/N)")
        rematch = input().upper()
else:
    if (rematch == "N"):
        print("Thank you for playing...")

