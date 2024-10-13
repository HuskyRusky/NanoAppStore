from colorama import Fore, Back, Style, init
init()
import random
import os
import time

Red = (f"{Back.RED} {Style.RESET_ALL}") #This are all the available colors, The reason why it says Style.reset_all at the end, is because if that isn't ther it will make the whole line it is on, the color that it is
Blue = (f"{Back.BLUE} {Style.RESET_ALL}")
Yellow = (f"{Back.YELLOW} {Style.RESET_ALL}")
Cyan = (f"{Back.CYAN} {Style.RESET_ALL}")
Magenta = (f"{Back.MAGENTA} {Style.RESET_ALL}")
Green = (f"{Back.GREEN} {Style.RESET_ALL}")
ColorList = [Red, Blue, Yellow, Cyan, Magenta, Green]

Gray = (f"{Back.LIGHTBLACK_EX} {Style.RESET_ALL}")
White = (f"{Back.WHITE} {Style.RESET_ALL}")

    


def MasterMindGameStart():
    """
    This is the function that starts the game.
    The code will create a randomly created color code and user has to guess it
    If the user guesses a correct color and it is at the right spot, it will be displayed randomly at the left side of the board with a gray color.
    If the user guesses a correct color but it is not at the right spot, it will be desplayed randomly at the left side of the board with a white color.
    If the user guesses 10 times in a row but didn't fully fill in the color code, then the user loses.
    If the user guesses the color code correctly within 10 tries, then the user wins the game.
    """
    MasterMindBoard = (f"|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n")
    ColorOptions = (f"1 = {Red}\n2 = {Blue}\n3 = {Yellow}\n4 = {Cyan}\n5 = {Magenta}\n6 = {Green}")
    CodeList = []
    MasterMindBoardList = list(MasterMindBoard) #A copy of the board is saved into a list, because a list editable, while a string is not editable
    while len(CodeList) < 4:
        RandomColor = random.choice(ColorList)
        if RandomColor not in CodeList:
            CodeList.append(RandomColor)
    Code = ''.join(CodeList)
    print(MasterMindBoard)
    NextLineJump = 0
    while True:
        while True:
            try:
                print(ColorOptions)
                ColorOneChose = input("\nChoose what you want as the first color\n\n")
                if ColorOneChose == "1":
                    ColorOne = Red
                    break
                elif ColorOneChose == "2":
                    ColorOne = Blue
                    break
                elif ColorOneChose == "3":
                    ColorOne = Yellow
                    break
                elif ColorOneChose == "4":
                    ColorOne = Cyan
                    break
                elif ColorOneChose == "5":
                    ColorOne = Magenta
                    break
                elif ColorOneChose == "6":
                    ColorOne = Green
                    break
                else:
                    print("\nPlease choose one of the available options")
                    time.sleep(1)
                    os.system('cls')
            except KeyboardInterrupt:
                print("\nPlease choose one of the available options")
                time.sleep(1)
                os.system('cls')
        os.system('cls')
        while True:
            try:
                print(MasterMindBoard)
                print(ColorOptions)
                ColorTwoChose = input("\nChoose what you want as the second color\n\n")
                if ColorTwoChose == ColorOneChose:
                    print("You can only choose a color that you didn't choose before")
                    time.sleep(1)
                    os.system('cls')
                elif ColorTwoChose == "1":
                    ColorTwo = Red
                    break
                elif ColorTwoChose == "2":
                    ColorTwo = Blue
                    break
                elif ColorTwoChose == "3":
                    ColorTwo = Yellow
                    break
                elif ColorTwoChose == "4":
                    ColorTwo = Cyan
                    break
                elif ColorTwoChose == "5":
                    ColorTwo = Magenta
                    break
                elif ColorTwoChose == "6":
                    ColorTwo = Green
                    break
                else:
                    print("\nPlease choose one of the available options")
                    time.sleep(1)
                    os.system('cls')
            except KeyboardInterrupt:
                print("\nPlease choose one of the available options")
                time.sleep(1)
                os.system('cls')
        os.system('cls')
        while True:
            try:
                print(MasterMindBoard)
                print(ColorOptions)
                ColorThreeChose = input("\nChoose what you want as the third color\n\n")
                if ColorThreeChose == ColorTwoChose or ColorThreeChose == ColorOneChose:
                    print("You can only choose a color that you didn't choose before")
                    time.sleep(1)
                    os.system('cls')
                elif ColorThreeChose == "1":
                    ColorThree = Red
                    break
                elif ColorThreeChose == "2":
                    ColorThree = Blue
                    break
                elif ColorThreeChose == "3":
                    ColorThree = Yellow
                    break
                elif ColorThreeChose == "4":
                    ColorThree = Cyan
                    break
                elif ColorThreeChose == "5":
                    ColorThree = Magenta
                    break
                elif ColorThreeChose == "6":
                    ColorThree = Green
                    break
                else:
                    print("\nPlease choose one of the available options")
                    time.sleep(1)
                    os.system('cls')
            except KeyboardInterrupt:
                print("\nPlease choose one of the available options")
                time.sleep(1)
                os.system('cls')
        os.system('cls')
        while True:
            try:
                print(MasterMindBoard)
                print(ColorOptions)
                ColorFourChose = input("\nChoose what you want as the fourth color\n\n")
                if ColorFourChose == ColorThreeChose or ColorFourChose == ColorTwoChose or ColorFourChose == ColorOneChose:
                    print("You can only choose a color that you didn't choose before")
                    time.sleep(1)
                    os.system('cls')
                elif ColorFourChose == "1":
                    ColorFour = Red
                    break
                elif ColorFourChose == "2":
                    ColorFour = Blue
                    break
                elif ColorFourChose == "3":
                    ColorFour = Yellow
                    break
                elif ColorFourChose == "4":
                    ColorFour = Cyan
                    break
                elif ColorFourChose == "5":
                    ColorFour = Magenta
                    break
                elif ColorFourChose == "6":
                    ColorFour = Green
                    break
                else:
                    print("\nPlease choose one of the available options")
                    time.sleep(1)
                    os.system('cls')
            except KeyboardInterrupt:
                print("\nPlease choose one of the available options")
                time.sleep(1)
                os.system('cls')
        os.system('cls')
        UserColorList = [ColorOne, ColorTwo, ColorThree, ColorFour]
        MasterMindBoardList[114 - NextLineJump] = ColorOne #This is to print the colors that user guessed on the screen, the nextlimejump is used to go the next line on the board
        MasterMindBoardList[115 - NextLineJump] = ColorTwo
        MasterMindBoardList[116 - NextLineJump] = ColorThree
        MasterMindBoardList[117 - NextLineJump] = ColorFour
        MasterMindBoard = ''.join(MasterMindBoardList)
        
        while True: #This is used to display the colors that user guessed correctly, and it is done so that the displayed colors are in a random order
            RandomAnswer = random.randint(109 - NextLineJump, 112 - NextLineJump)
            if ColorOne == CodeList[0]:
                if MasterMindBoardList[RandomAnswer] != Gray and MasterMindBoardList[RandomAnswer] != White:
                    MasterMindBoardList[RandomAnswer] = Gray
                    break
            elif ColorOne in CodeList:
                if MasterMindBoardList[RandomAnswer] != Gray and MasterMindBoardList[RandomAnswer] != White:
                    MasterMindBoardList[RandomAnswer] = White
                    break
            else:
                break
        while True:
            RandomAnswer = random.randint(109 - NextLineJump, 112 - NextLineJump)
            if ColorTwo == CodeList[1]:
                if MasterMindBoardList[RandomAnswer] != Gray and MasterMindBoardList[RandomAnswer] != White:
                    MasterMindBoardList[RandomAnswer] = Gray
                    break
            elif ColorTwo in CodeList:
                if MasterMindBoardList[RandomAnswer] != Gray and MasterMindBoardList[RandomAnswer] != White:
                    MasterMindBoardList[RandomAnswer] = White
                    break
            else:
                break
        while True:
            RandomAnswer = random.randint(109 - NextLineJump, 112 - NextLineJump)
            if ColorThree == CodeList[2]:
                if MasterMindBoardList[RandomAnswer] != Gray and MasterMindBoardList[RandomAnswer] != White:
                    MasterMindBoardList[RandomAnswer] = Gray
                    break
            elif ColorThree in CodeList:
                if MasterMindBoardList[RandomAnswer] != Gray and MasterMindBoardList[RandomAnswer] != White:
                    MasterMindBoardList[RandomAnswer] = White
                    break
            else:
                break
        while True:
            RandomAnswer = random.randint(109 - NextLineJump, 112 - NextLineJump)
            if ColorFour == CodeList[3]:
                if MasterMindBoardList[RandomAnswer] != Gray and MasterMindBoardList[RandomAnswer] != White:
                    MasterMindBoardList[RandomAnswer] = Gray
                    break
            elif ColorFour in CodeList:
                if MasterMindBoardList[RandomAnswer] != Gray and MasterMindBoardList[RandomAnswer] != White:
                    MasterMindBoardList[RandomAnswer] = White
                    break
            else:
                break


        MasterMindBoard = ''.join(MasterMindBoardList) #This saves whatever was edited in the list as the new board string
        NextLineJump = NextLineJump + 12
        print(MasterMindBoard)
        if UserColorList == CodeList:
            print("\nYou won the game\n")
            PlayAgain()
            
        elif NextLineJump == 120:
            print("\nYou lost the game\n")
            print(f"The code was {Code}")
            PlayAgain()
            

def PlayAgain():
    """
    This is the function that asks the user if the user wants to play again or not.
    If the user chooses yes, then the MasterMindGameStart function will be called and the game will be started again.
    If the user chooses no, then the Nano appstore will be opened.
    """
    while True:
            try:
                Again = input("\nDo you want to play again, yes or no?\n\n").lower()
                os.system('cls')
                if Again == "yes":
                    MasterMindGameStart()
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

        
        


def MasterMindStart():
    """
    This is the function where the program starts.
    Ther is an explanation on how the game works.
    If the user understands the game, the user can type yes and the MasterMindGameStart function will be called, and the game will be started.
    """
    while True:
        try:
            os.system('cls')
            print("Welcome to mastermind\n")
            print("Here is an explanation on how the game works\n")
            print((f"|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n|____:____|\n"))
            print(f"1 = {Red}\n2 = {Blue}\n3 = {Yellow}\n4 = {Cyan}\n5 = {Magenta}\n6 = {Green}")
            print("\nThis is the board and the available options to choose from")
            print("Ther is a color code, that you have to guess")
            print("After you guessed four colors, four squares on the left of the board will get the color white, gray or no color")
            print("Gray means, you got a color right")
            print("White means you got a color right, but at the right position")
            print("No color means, that you got a color not right")
            print("Keep in mind that the squares are randomly filled with a color, that means that it won't reveal which color\nyou got right or which one you got wrong\n")
    
            UserReady = input("Are you ready to play the game? type yes if you are ready\n\n").lower()
            if UserReady == "yes":
                os.system('cls')
                MasterMindGameStart()
            else:
                print("You can only type in yes")
                time.sleep(1)
        except KeyboardInterrupt:
                print("You can only type in yes")
                time.sleep(1)

















#Bronnen

#Van chatgpt heb ik geleerd hoe je tekst of achtergronden van tekst een kleur kan geven
#https://chatgpt.com/c/670bade7-4e48-800f-8b52-79f813a784dc
#https://chatgpt.com/c/670bb673-eac0-800f-8bae-6024243d57de