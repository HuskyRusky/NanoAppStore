import random
from subprocess import call
import datetime
import os
import time




def HangManGame(DifficultyUser, NameUser):
    """
    In this function is the game played. Everytime the user guesses a correct letter, it will print out the correct letters and on which spot they are in the word.
    If the user guesses a letter the user already guessed right or the user guessed a letter the user already guessed wrong then it will be printed on the screen, that the user already guessed this wrong or right.
    If the user guesses wrong, then the user will lose 1 try and if the try counter reaches 0, then the game is over.
    If the user finds the correct word, that means that the user won the game.
    At the end of the game, the user is asked if the user wants to play the game again or not.
    If the user chooses yes, the game will be played again, but if the user chooses no, then the Nano appstore will be opened.
    The score will also be saved in the score.txt file.
    """
    AlleWoorden = open("GalgjeWoorden.txt")
    Difficulty = AlleWoorden.readlines()
    Easy = Difficulty[random.randint(2,21)] #This is so that it picks the words that are from line 2 to 24 in the txt file
    Medium = Difficulty[random.randint(25,44)]
    Hard = Difficulty[random.randint(48,67)]
    
    Tries = 11
    WrongAnswers = ""
    AlleWoorden.close()
    if DifficultyUser == "1" or DifficultyUser == "easy":
        Word = Easy
        GuessWord = len(Easy) - 1
        GuessWord = ("_" * GuessWord)
        WordLijst = list(GuessWord)
    elif DifficultyUser == "2" or DifficultyUser == "medium":
        Word = Medium
        GuessWord = len(Medium) - 1
        GuessWord = ("_" * GuessWord)
        WordLijst = list(GuessWord)
    elif DifficultyUser == "3" or DifficultyUser == "hard":
        Word = Hard
        GuessWord = len(Hard) - 1
        GuessWord = ("_" * GuessWord)
        WordLijst = list(GuessWord)
    WordLettersLeft = list(Word)
    print("\nGuess the word\n")
    print(f"You have {Tries} tries\n")
    print("Voer een letter in\n")
    print(f"{GuessWord}\n")
    while Tries > 0:
        try:
            if GuessWord in Word:
                print("\nYou guessed the word correctly\n")
                Result = "Won"
                Score(Tries, Word, Result, NameUser)
            UserGuess = str(input())
            if len(UserGuess) == 1:
                for Guess in range (0, len(Word) - 1):
                    if UserGuess.isalpha() == False: #This prevents that the user types in something else that is not a letter
                        os.system('cls')
                        print("\nYou can only put it in one letter\n")
                        print(f"\n                                                                  Wrong letters {WrongAnswers}\n")
                        print(f"You have {Tries}, tries left\n")
                        print(f"{GuessWord}\n")
                        break
                    elif UserGuess in Word[Guess]:
                        WordLijst[Guess] = UserGuess
                        if UserGuess in GuessWord and UserGuess not in WordLettersLeft: #If the user tries to guess a letter, that the user already guessed correctly, then it will print that the user already guessed this letter correctly
                            os.system('cls')
                            print("\nYou already guessed this letter correctly\n")
                            print(f"\n                                                                  Wrong letters {WrongAnswers}\n")
                            print(f"You have {Tries}, tries left\n")
                            print(f"\n{GuessWord}\n")
                        else:
                            os.system('cls')
                            GuessWord = "".join(WordLijst)
                            WordLettersLeft[Guess] = ""
                            print(f"\n                                                                  Wrong letters {WrongAnswers}\n")
                            print(f"You have {Tries}, tries left\n")
                            print(f"{GuessWord}\n")
                    elif UserGuess not in Word and UserGuess in WrongAnswers: #If the user tries to guess a letter that the user already guessed wrong, then it will print that the user already guessed this letter wrong
                        os.system('cls')
                        print(f"\nYou already guessed this letter wrong                             Wrong letters {WrongAnswers}\n")
                        print(f"You have {Tries}, tries left\n")
                        print(f"{GuessWord}\n")
                        break
                    elif UserGuess not in Word: #If the user guesses a wrong letter, it will be printed to the screen
                        WrongAnswers = WrongAnswers + UserGuess
                        os.system('cls')
                        print(f"\nYou made a wrong guess                             Wrong letters {WrongAnswers}\n")
                        Tries = Tries - 1
                        print(f"You have {Tries}, tries left\n")
                        print(f"{GuessWord}\n")
                        break
            else:
                os.system('cls')
                print("\nYou can only put it in one letter\n")
                print(f"\n                                                                  Wrong letters {WrongAnswers}\n")
                print(f"You have {Tries}, tries left\n")
                print(f"{GuessWord}\n")
        except KeyboardInterrupt:
            os.system('cls')
            print("\nYou can only put it in one letter\n")
            print(f"\n                                                                  Wrong letters {WrongAnswers}\n")
            print(f"You have {Tries}, tries left\n")
            print(f"{GuessWord}\n")
    if Tries == 0:
        Result = "Lost"
        print("You lost")
        print(f"The word was {Word}")
        Score(Tries, Word, Result, NameUser)

def Score(UserTries, Word, Result, NameUser):
    """
    In this function, the score is being saved into txt file
    It adds information to the score such as, the name of the user, the time, and the date
    """
    Time = datetime.datetime.now()
    TimeUser = (f"{Time.year}-{Time.month}-{Time.day} {Time.hour}:{Time.minute}")
    ScoreTxt = open("Score.txt","a")
    #ScoreList = (f"Name = {NameUser}\n",f"Date and time = {TimeUser}\n",f"Tries = {AmountOfTries}\n",f"Word = {Word}\n",f"Result = {Result}")
    ScoreList = (f"Name = {NameUser}\nDate and time = {TimeUser}\nTries left = {UserTries}/11\nWord = {Word}Result = {Result}\n\n\n\n")
    ScoreTxt.write(ScoreList)
    ScoreTxt.close()
    PlayAgain()


def PlayAgain():
    """
    This is the function that makes the user decide if the user wants to play again or not.
    If the user types yes, the game will be started again and if the user types no, then the Nano appstore will be opened.
    """
    while True:
        try:
            Again = input("Do you want to play again, yes or no?\n\n").lower()
            os.system('cls')
            if Again == "yes":
                HangManStart()
            elif Again == "no":
                import NanoAppStore
                NanoAppStore.UserChose()
            else:
                print("\nPlease type in yes or no\n")
        except KeyboardInterrupt:
            print("Please type in yes or no\n")
            time.sleep(1)
            os.system('cls')




def HangManStart():
    """
    This is where program starts, and it asks for the name of the user.
    It also asks which difficulty the user wants to play.
    After the choses, the caller will send those choses to the hangmangame function that starts the game.
    """
    while True:
        try:
            print("\nWelcome to hangman\n")
            UserName = input("What is your name?\n\n")
            if len(UserName) == 0:
                print("Please enter atleast one number or letter")
                time.sleep(1)
                os.system('cls')
            else:
                os.system('cls')
                break
        except KeyboardInterrupt:
            print("Please enter atleast one number or letter")
            time.sleep(1)
            os.system('cls')
    while True:
        try:
            print("\nTo start, please enter a difficulty")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            print("")
            DifficultyChose = input().lower()
            if DifficultyChose == "1" or DifficultyChose == "easy" or DifficultyChose == "2" or DifficultyChose == "medium" or DifficultyChose == "3" or DifficultyChose == "hard":
                os.system('cls')
                HangManGame(DifficultyChose, UserName)
                break
            else:
                print("Please enter one of the available options")
                time.sleep(1)
                os.system('cls')
        except KeyboardInterrupt:
            print("Please enter one of the available options")
            time.sleep(1)
            os.system('cls')






























#Bronnen
#
#Dit gebruikte ik om een specifieke line in een txt toe te passen in de code
#https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/
#
#Dit gebruikte ik om te leren hoe je kan detecteren of de user input letters zijn
#https://www.tutorialspoint.com/how-to-check-if-a-character-in-a-string-is-a-letter-in-python#:~:text=We%20use%20the%20isalpha(),message%20based%20on%20the%20result.