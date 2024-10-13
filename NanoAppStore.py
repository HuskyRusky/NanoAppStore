import GuessingGame
import HangMan
import TicTacToe
import RockPaperScissors
import Mastermind
import os
import time
    



def UserChose():
    """
    In this function, the user can decide which game the user wants to play.
    """
    while True:
        try:
            print("\nSelect a game name or number out of the list\n")
            print("\n1. Guessing game")
            print("2. Hangman")
            print("3. Tic-tac-toe")
            print("4. Rock paper scissors")
            print("5. Mastermind\n")
            UserInput = input().lower()
            os.system('cls')
            if UserInput in ["guessing game", "1"]:
                GuessingGame.GuessingGameStart()
            elif UserInput in ["hangman", "2"]:
                HangMan.HangManStart()
            elif UserInput in ["tic-tac-toe", "3"]:
                TicTacToe.TicTacToeStart()
            elif UserInput in ["Rock paper scissors", "4"]:
                RockPaperScissors.RockPaperScissorsStart()
            elif UserInput in ["Mastermind", "5"]:
                Mastermind.MasterMindStart()
            else:
                print("\nPlease choose a game that is in the list")
                time.sleep(1)
                os.system('cls')
        except KeyboardInterrupt:
            print("\nPlease choose a game that is in the list")
            time.sleep(1)
            os.system('cls')
    


UserChose()




#Bronnen
#Dit gebruikte ik om erachter te komen hoe de hele command line interface can clearen
#https://stackoverflow.com/questions/63984945/clear-command-line-in-python-and-microsoft-visual-studio