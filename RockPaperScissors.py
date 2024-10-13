import time
import random
import os


def RockPaperScissorsGame(PlayerComputer):
    """
    This is where the game starts, if the user decided to play against the computer, then ther will be only input for one player and the computer makes random moves.
    If the user decided to play against another player, it will be said to not look on the screen while the other playing is choosing a move.
    The game ends if one of the players or if the computer gets to 3 wins.
    After the game ends, it is asked if the user wants to play again or not.
    """
    try:
        Options = ["Rock", "Paper", "Scissors"]
        PlayerOneWins = 0
        ComputerOrPlayerTwoWins = 0
        if PlayerComputer == "1":
            print("\nYou are up against bot Yoris\n")
            print("First to 3 wins\n")
            print("Yoris : I am going to beat you")
            print("HE IS TAUNTING YOU FAST CHOOSE ROCK, PAPER OR SCISSORS\n")

        if PlayerComputer == "2":
            print("\nMake sure the other player is not looking on the screen while you are choosing your move\n")
            print("First to 3 wins\n")
            print("Let the game begin\n")
        while True:
            while True:
                try:
                    if PlayerComputer == "1":
                        PlayerOneMove = input("1. Rock 2. Paper 3. Scissors\n\n")
                        os.system('cls')
                    if PlayerComputer == "2":
                        PlayerOneMove = input("Player one make your move\n1. Rock 2. Paper 3. Scissors\n\n")
                        os.system('cls')
                    if PlayerOneMove == "1" or PlayerOneMove == "Rock":
                        PlayerOneMove = "Rock"
                        break
                    elif PlayerOneMove == "2" or PlayerOneMove == "Paper":
                        PlayerOneMove = "Paper"
                        break
                    elif PlayerOneMove == "3" or PlayerOneMove == "Scissors":
                        PlayerOneMove = "Scissors"
                        break
                    else:
                        os.system('cls')
                        print("Please type in the number or the name of your chose")
                except KeyboardInterrupt:
                    os.system('cls')
                    print("Please type in the number or the name of your chose")
            if PlayerComputer == "1":
                ComputerOrPlayerTwoMove = Options[random.randint(0, 2)]
            if PlayerComputer == "2":
                while True:
                    try:
                        ComputerOrPlayerTwoMove = input("Player two make your move\n1. Rock 2. Paper 3. Scissors\n\n")
                        os.system('cls')
                        if ComputerOrPlayerTwoMove == "1" or ComputerOrPlayerTwoMove == "Rock":
                            ComputerOrPlayerTwoMove = "Rock"
                            break
                        elif ComputerOrPlayerTwoMove == "2" or ComputerOrPlayerTwoMove == "Paper":
                            ComputerOrPlayerTwoMove = "Paper"
                            break
                        elif ComputerOrPlayerTwoMove == "3" or ComputerOrPlayerTwoMove == "Scissors":
                            ComputerOrPlayerTwoMove = "Scissors"
                            break
                        else:
                            os.system('cls')
                            print("Please type in the number or the name of your chose")
                    except KeyboardInterrupt:
                        os.system('cls')
                        print("Please type in the number or the name of your chose")
            print("Here we go\n")
            print("Rock\n")
            time.sleep(1) #This is so that it makes the game feel smoother, instead of rock paper scissors being printed instantly, it takes a second between each word
            print("Paper\n")
            time.sleep(1)
            print("Scissors\n")
            time.sleep(1)
            if PlayerComputer == "1":
                print(f"You chose {PlayerOneMove}\n")
            if PlayerComputer == "1":
                print(f"Yoris choose {ComputerOrPlayerTwoMove}\n")
            elif PlayerComputer == "2":
                print(f"Player one chose {PlayerOneMove}\n")
                print(f"Player two chose {ComputerOrPlayerTwoMove}\n")
            if PlayerOneMove == "Rock" and ComputerOrPlayerTwoMove == "Paper":
                if PlayerComputer == "1":
                    print("Yoris won\n")
                    print("Yoris : Ha That was too easy\n")
                    ComputerOrPlayerTwoWins = ComputerOrPlayerTwoWins + 1
                    print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
                elif PlayerComputer == "2":
                    print("Player two won")
                    ComputerOrPlayerTwoWins = ComputerOrPlayerTwoWins + 1
                    print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
            elif PlayerOneMove == "Rock" and ComputerOrPlayerTwoMove == "Rock":
                print("Its a draw\n")
                print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
            elif PlayerOneMove == "Rock" and ComputerOrPlayerTwoMove == "Scissors":
                print("Player one won")
                PlayerOneWins = PlayerOneWins + 1
                print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
            if PlayerOneMove == "Paper" and ComputerOrPlayerTwoMove == "Scissors":
                if PlayerComputer == "1":
                    print("Yoris won\n")
                    print("Yoris : Ha That was too easy\n")
                    ComputerOrPlayerTwoWins = ComputerOrPlayerTwoWins + 1
                    print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
                elif PlayerComputer == "2":
                    print("Player two won")
                    ComputerOrPlayerTwoWins = ComputerOrPlayerTwoWins + 1
                    print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
            elif PlayerOneMove == "Paper" and ComputerOrPlayerTwoMove == "Paper":
                print("Its a draw\n")
                print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
            elif PlayerOneMove == "Paper" and ComputerOrPlayerTwoMove == "Rock":
                print("Player one won")
                PlayerOneWins = PlayerOneWins + 1
                print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
            if PlayerOneMove == "Scissors" and ComputerOrPlayerTwoMove == "Rock":
                if PlayerComputer == "1":
                    print("Yoris won\n")
                    print("Yoris : Ha That was too easy\n")
                    ComputerOrPlayerTwoWins = ComputerOrPlayerTwoWins + 1
                    print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
                elif PlayerComputer == "2":
                    print("Player two won")
                    ComputerOrPlayerTwoWins = ComputerOrPlayerTwoWins + 1
                    print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
            elif PlayerOneMove == "Scissors" and ComputerOrPlayerTwoMove == "Scissors":
                print("Its a draw\n")
                print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
            elif PlayerOneMove == "Scissors" and ComputerOrPlayerTwoMove == "Paper":
                print("Player one won")
                PlayerOneWins = PlayerOneWins + 1
                print(f"{PlayerOneWins} - {ComputerOrPlayerTwoWins}\n")
            if PlayerOneWins == 3 or ComputerOrPlayerTwoWins == 3:
                break
        if PlayerOneWins == 3 and PlayerComputer == "1":
            print("You won the game\n")
            print("Yoris : Arrrrggghhhh")
        elif PlayerOneWins == 3 and PlayerComputer == "2":
            print("Player one won the game")
        elif ComputerOrPlayerTwoWins == 3 and PlayerComputer == "1":
            print("Yoris won the game")
            print("Yoris : Give me a real opponent next time")
        elif ComputerOrPlayerTwoWins == 3 and PlayerComputer == "2":
            print("Player two won the game")
        while True:
            try:
                Again = input("\nDo you want to play again, yes or no?\n\n").lower()
                os.system('cls')
                if Again == "yes":
                    RockPaperScissorsStart()
                elif Again == "no":
                    import NanoAppStore
                    NanoAppStore.UserChose()
                else:
                    print("\nPlease type in yes or no\n")
                    time.sleep(1)
                    os.system('cls')
            except KeyboardInterrupt:
                print("\nPlease type in yes or no\n")
                time.sleep(1)
                os.system('cls')
    except KeyboardInterrupt: #If the user types keyboard inputs that interact with the commandline interface for example crl + c while its not asked from user to type anything then it will restart the programm
        print("Please don't type in any words while not asked to")
        print("Restarting the programm")
        time.sleep(3)
        os.system('cls')
        RockPaperScissorsStart()


        







def RockPaperScissorsStart():
    """
    This is where the program starts, the user gets a chose if the user wants to play against the computer or against another player.
    After the decision, the caller will send the chose to the rockpaperscissorsgame function, which will start the game.
    """
    while True:
        print("Welcome to rock paper scissors\n")
        try:
            UserChose = input("Do you want to play 1. Against the computer 2. Against another player\nPlease type in a number corresponding to the option\n\n")
            if UserChose == "1" or UserChose == "2":
                os.system('cls')
                RockPaperScissorsGame(UserChose)
                break
            else:
                print("Please choose on the available options")
                time.sleep(1)
                os.system('cls')
        except KeyboardInterrupt:
            print("Please choose on the available options")
            time.sleep(1)
            os.system('cls')