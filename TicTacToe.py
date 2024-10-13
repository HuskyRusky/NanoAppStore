import os
import time


def TicTacToeStart():
    """
    The whole game is played inside of this function and is a 2 players game, first ther is an explanation how the game board works.
    After the player chooses a square to put his X or O in, the code checks if 3 X's or 3 O's are connected.
    If 3 X's or 3 O's are connected, then the game ends and the player that had them connected wins.
    At the end, it is asked if the players want to play again or not. If they choose not to play again, then the Nano appstore will opened.
    """

    print("\nWelcome to tic-tac-toe\n")
    print("This the playing area, you have to type in the number that corresponds\nto the square that you want to put your X or O into\n\n")
    Board = (" . . . .\n .1.2.3. \n .4.5.6.\n .7.8.9. ")
    print(Board) #This is the board and it shows the numbers from 1 to 9 assigned to ther own square
    ListBoard = list(Board)


    while True:
        while True:
            #This is the code for player 1
            try:
                PlayerInput = input("\n\n\n\nPlayer 1, it is your turn\n\n")
                os.system('cls')
                if PlayerInput == "1":
                    if ListBoard[11] == "X":
                        print("You already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[11] == "O":
                        print("Your opponent already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[11] = "X"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "2":
                    if ListBoard[13] == "X":
                        print("You already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[13] == "O":
                        print("Your opponent already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[13] = "X"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "3":
                    if ListBoard[15] == "X":
                        print("You already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[15] == "O":
                        print("Your opponent already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[15] = "X"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "4":
                    if ListBoard[21] == "X":
                        print("You already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[21] == "O":
                        print("Your opponent already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[21] = "X"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "5":
                    if ListBoard[23] == "X":
                        print("You already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[23] == "O":
                        print("Your opponent already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[23] = "X"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "6":
                    if ListBoard[25] == "X":
                        print("You already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[25] == "O":
                        print("Your opponent already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[25] = "X"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "7":
                    if ListBoard[30] == "X":
                        print("You already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[30] == "O":
                        print("Your opponent already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[30] = "X"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "8":
                    if ListBoard[32] == "X":
                        print("You already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[32] == "O":
                        print("Your opponent already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[32] = "X"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "9":
                    if ListBoard[34] == "X":
                        print("You already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[34] == "O":
                        print("Your opponent already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[34] = "X"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                else:
                    print("Please type in one of the available options")
                    time.sleep(1)
                    os.system('cls')
                    print(f"\n\n\n\n\n{Board}")
            except KeyboardInterrupt:
                print("Please type in one of the available options")
                time.sleep(1)
                os.system('cls')
                print(f"\n\n\n\n\n{Board}")
        if (ListBoard[11] == "X" and ListBoard[13] == "X" and ListBoard[15] == "X" #This is a check if 3 X's are connected
            or ListBoard[11] == "X" and ListBoard[21] == "X" and ListBoard[30] == "X"
            or ListBoard[11] == "X" and ListBoard[23] == "X" and ListBoard[34] == "X"
            or ListBoard[13] == "X" and ListBoard[23] == "X" and ListBoard[32] == "X"
            or ListBoard[15] == "X" and ListBoard[25] == "X" and ListBoard[34] == "X"
            or ListBoard[15] == "X" and ListBoard[23] == "X" and ListBoard[30] == "X"
            or ListBoard[21] == "X" and ListBoard[23] == "X" and ListBoard[25] == "X"
            or ListBoard[30] == "X" and ListBoard[32] == "X" and ListBoard[34] == "X"
           ):
            print("\nPlayer 1 won the game")
            break
        elif ( "1" not in ListBoard[11] and "2" not in ListBoard[13] and "3" not in ListBoard[15]
            and "4" not in ListBoard[21] and "5" not in ListBoard[23] and "6" not in ListBoard[25]
            and "7" not in ListBoard[30] and "8" not in ListBoard[32] and "9" not in ListBoard[34]
           ):
            print("\nIts a draw")
            break
        #This is the code for player 2
        while True:
            try:
                PlayerInput = input("\n\n\n\nPlayer 2, it is your turn\n\n")
                os.system('cls')
                if PlayerInput == "1":
                    if ListBoard[11] == "O":
                        print("You already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[11] == "X":
                        print("Your opponent already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[11] = "O"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "2":
                    if ListBoard[13] == "O":
                        print("You already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[13] == "X":
                        print("Your opponent already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[13] = "O"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "3":
                    if ListBoard[15] == "O":
                        print("You already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[15] == "X":
                        print("Your opponent already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[15] = "O"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "4":
                    if ListBoard[21] == "O":
                        print("You already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[21] == "X":
                        print("Your opponent already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[21] = "O"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "5":
                    if ListBoard[23] == "O":
                        print("You already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[23] == "X":
                        print("Your opponent already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[23] = "O"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "6":
                    if ListBoard[25] == "O":
                        print("You already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[25] == "X":
                        print("Your opponent already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[25] = "O"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "7":
                    if ListBoard[30] == "O":
                        print("You already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[30] == "X":
                        print("Your opponent already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[30] = "O"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "8":
                    if ListBoard[32] == "O":
                        print("You already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[32] == "X":
                        print("Your opponent already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[32] = "O"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                if PlayerInput == "9":
                    if ListBoard[34] == "O":
                        print("You already put a O on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    elif ListBoard[34] == "X":
                        print("Your opponent already put a X on this square, please choose a different square\n")
                        print(f"\n\n\n\n\n{Board}")
                    else:
                        ListBoard[34] = "O"
                        Board = "".join(ListBoard)
                        print(f"\n\n\n\n\n{Board}")
                        break
                else:
                    print("Please type in one of the available options")
                    time.sleep(1)
                    os.system('cls')
                    print(f"\n\n\n\n\n{Board}")
                if PlayerInput != "1" and PlayerInput != "2" and PlayerInput != "3" and PlayerInput != "4" and PlayerInput != "5" and PlayerInput != "6" and PlayerInput != "7" and PlayerInput != "8" and PlayerInput != "9":
                        print("You can only put in a number from 1 to 9")
            except KeyboardInterrupt:
                print("Please type in one of the available options")
                time.sleep(1)
                os.system('cls')
                print(f"\n\n\n\n\n{Board}")
        if (ListBoard[11] == "O" and ListBoard[13] == "O" and ListBoard[15] == "O"
            or ListBoard[11] == "O" and ListBoard[21] == "O" and ListBoard[30] == "O"
            or ListBoard[11] == "O" and ListBoard[23] == "O" and ListBoard[34] == "O"
            or ListBoard[13] == "O" and ListBoard[23] == "O" and ListBoard[32] == "O"
            or ListBoard[15] == "O" and ListBoard[25] == "O" and ListBoard[34] == "O"
            or ListBoard[15] == "O" and ListBoard[23] == "O" and ListBoard[30] == "O"
            or ListBoard[21] == "O" and ListBoard[23] == "O" and ListBoard[25] == "O"
            or ListBoard[30] == "O" and ListBoard[32] == "O" and ListBoard[34] == "O"
           ):
            print("\nPlayer 2 won the game")
            break
        elif ( "1" not in ListBoard[11] and "2" not in ListBoard[13] and "3" not in ListBoard[15]
            and "4" not in ListBoard[21] and "5" not in ListBoard[23] and "6" not in ListBoard[25]
            and "7" not in ListBoard[30] and "8" not in ListBoard[32] and "9" not in ListBoard[34]
           ):
            print("Its a draw")
            break
    while True:
        Again = input("\nDo you want to play again, yes or no?\n\n").lower()
        os.system('cls')
        if Again == "yes":
            TicTacToeStart()
        elif Again == "no":
            import NanoAppStore
            NanoAppStore.UserChose()
        else:
            print("\nPlease type in yes or no\n")
