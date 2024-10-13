import random
import os

def ExitGame():
    print("Type again, if you want to play again")
    print("Type exit, if you want to stop playing\n")
    Again = "again"
    Exit = "exit"
    UserAgain = input().lower()
    os.system('cls')
    if UserAgain == Again:
        GuessingGameStart()
    elif UserAgain == Exit:
        import NanoAppStore
        NanoAppStore.UserChose()
    else:
        print("")
        print("You can't type something else other than again or exit")
        ExitGame()

def GuessingGameStart():
    RandomInt = random.randint(1, 100)
    AttemptsLeft = 11

    print("\nWelcome in this game, you have to guess the number between 1 and 100")
    print("Everytime you put in the wrong answer, you will be told if its lower or higher then your answer")
    print("You have 10 attempts to guess the number between 1 and 100")
    print("To start, enter a random number between 1 and 100\n")

    while True:
        try:
            AnswerUser = int(input())
        except (ValueError, KeyboardInterrupt):
            print("\nType in a number please\n")
        else:
            if AnswerUser == RandomInt:
                print("")
                print("You found the correct number")
                ExitGame()
            else:
                AttemptsLeft = AttemptsLeft - 1
                print("")
                print("Your answer was wrong")
                print("You have", (AttemptsLeft), "attempts left")
            if AnswerUser < RandomInt:
                print("Your answer was a smaller number then the correct number\n")
            elif AnswerUser > RandomInt:
                print("Your answer was a larger number then the correct number\n")
            if AttemptsLeft == 0:
                print("")
                print("You have no attempts left\n")
                ExitGame()






