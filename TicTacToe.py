import re

def drawBoard(size,game):
    rows = 0
    while( rows != size):
        print(" ",end="")
        for i in range(size):
            print("-"*size,end=" ")
        print("")
        for j in range(size):
            symbol = game[rows][j]
            if(symbol !=1):
             print("|",end=f" {symbol} ")
            else:
             print("|", end=" "*size)
        print("|")
        rows +=1
    print(" ", end="")
    for i in range(size):
        print("-" * size, end=" ")
    print("\n\n")




def checkWINNER(gameMATRIX, size): # returns either 'X' , '0' or NONE
    # to know weather a player has won or not , we need to check:
    # VERTICALLY :
    # a[0][0] = a[1][0] = a[2][0]
    # a[0][1] = a[1][1] = a[2][1]
    # a[0][2] = a[1][2] = a[2][2]

    # HORIZONTALLY
    # a[0][0] = a[0][1] = a[0][2]
    # a[1][0] = a[1][1] = a[1][2]
    # a[2][0] = a[2][1] = a[2][2]

    # DIAGONALLY

    # a[0][0] = a[1][1] = a[2][2]
    # a[0][2] = a[1][1] = a[2][0]

    # CHECK HORIZONTALLY
    for i in range(size):
        if (gameMATRIX[i][0] == gameMATRIX[i][1] == gameMATRIX[i][2] != 1):
                return gameMATRIX[i][0]

    # CHECK VERTICALLY
    for j in range(size):
        if (gameMATRIX[0][j] == gameMATRIX[1][j] == gameMATRIX[2][j] !=1):
                return gameMATRIX[0][j]

    # CHECK DIAGONALLY
    if (gameMATRIX[0][0] == gameMATRIX[1][1] == gameMATRIX[2][2] !=1 or (
            gameMATRIX[0][2] == gameMATRIX[1][1] == gameMATRIX[2][0] !=1)):
        return gameMATRIX[1][1]

    return "NONE"


def checkChoiceValidity(choice):
    valid_choice = re.compile(r'^\d,\d$')  # r stands for raw string
    match = valid_choice.search(choice)
    if (not match):
        print("please, enter a valid choice ( row,col) ")
        return 0
    row , col = choice.split(",")
    row = int(row)
    col = int(col)
    if( row < 1 or row > 3 or col < 1 or col > 3):
        print("you are out of range , choose numbers between [1 and 3]")
        return 0

    return 1


def takeChoiceFromPlayer(player):
    choice = input(f">>{player} , make your choice : ")
    validity = checkChoiceValidity(choice)
    if(validity == 0):
        return takeChoiceFromPlayer(player)
    return choice


def updateGame(game,player,move,symbol):
    move = move.split(",")
    row = int(move[0])-1
    col = int(move[1])-1

    if game[row][col] != 1:
        print("this move has already been played , choose another one ! ")
        updateGame(game,player,takeChoiceFromPlayer(player),symbol)
    else:game[row][col] = symbol

def isTheBoardFull(game):
    for row in game:
        for i in row:
            if i==1:
                return False
    print("There are no moves left !")
    return True



def start():
    game =   [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]



    boardSize = 3
    print("Hello ,welcome to tic tac toe game ! \n\n")
    player1 = input(" player 1 , please enter your name : ")
    player2 = input(" player 2 , please enter your name : ")


    print(f" {player1} , you will play as X")
    print(f" {player2} , you will play as 0")

    print("\n to choose the position , simply type rowNumber,columnNumber")
    print(" EXAMPLE >>player1 : 1,3 ( which is third column of the first row )\n")

    drawBoard(boardSize,game)
    print("")

    while(True):

        if (isTheBoardFull(game) == True):
            print("this is a draw !")
            break


        movePlayer1 = takeChoiceFromPlayer(player1)
        updateGame(game, player1, movePlayer1, 'X')
        print("\n\n#########UPDATE#############")

        drawBoard(boardSize,game)

        #checkwinner
        winner = checkWINNER(game, boardSize)
        if (winner == 'X'):
            print(f"{player1} has won !")
            break
        elif (winner == '0'):
            print(f"{player2} has won !")
            break
        else:

            if(isTheBoardFull(game) == True):
                 print("this is a draw ! ")
                 break

            movePlayer2 = takeChoiceFromPlayer(player2)
            updateGame(game, player2, movePlayer2, '0')
            print("\n\n#########UPDATE#############")
            drawBoard(boardSize,game)

            winner = checkWINNER(game, boardSize)
            if (winner == 'X'):
                print(f"{player1} has won !")
                break
            elif (winner == '0'):
                print(f"{player2} has won !")
                break
            else:
                if (isTheBoardFull(game) == True):
                    print("this is a draw ! ")
                    break














start()
""""
winner = checkWINNER(gameMATRIX,n)
if(winner == 0):
    print("DRAW")
elif(winner == 1):
    print("THE WINNER IS PLAYER 1")
else:
    print("WINNER IS PLAYER 2")"""






