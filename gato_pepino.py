

import numpy as np


def checkwin (board,value):
    win = False

    # rows
    for i in xrange(np.shape(board)[0]):
        if board[i,0]==board[i,1]==board[i,2]==value:
            win = True
        
    # columns
    for i in xrange(np.shape(board)[1]):
        print(np.sum(board[:,i]))
        if board[0,i]==board[1,i]==board[2,i]==value:
            win = True

    # diagonals
        if board[0,0]==board[1,1]==board[2,2]==value:
            win = True
        if board[0,2]==board[1,1]==board[2,0]==value:
            win = True
    return win

def isEven(num):
    return num % 2 == 0

def isOdd(num):
    return num % 2 != 0


# initialize game
board = np.array([[0,0,0],[0,0,0],[0,0,0]])
win = False

stage=0
while win == False:
    while isEven(stage):
        xcoord = raw_input("introduce la coordenada x de su tiro jugador 1  ")
        ycoord = raw_input("introduce la coordenada y de su tipo judador 1  ")
        try:
            xcoord = int(xcoord.strip())
            ycoord = int(ycoord.strip())
            if (0 <= xcoord <= 2) & (0 <= ycoord <= 2):
                if board[xcoord,ycoord]==0:
                    board[xcoord,ycoord]=1
                    win = checkwin(board,1)
                    stage=stage+1
        except ValueError:
            print("Vuelva a tirar")
            pass
    print(board)
    if win:
        print ("ganaste jugador 1")
        break
    while isOdd(stage):
        xcoord = raw_input("introduce la coordenada x de su tiro jugador 2  ")
        ycoord = raw_input("introduce la coordenada y de su tipo judador 2  ")
        try:
            xcoord = int(xcoord.strip())
            ycoord = int(ycoord.strip())
            if (0 <= xcoord <= 2) & (0 <= ycoord <= 2):
                if board[xcoord,ycoord]==0:
                    board[xcoord,ycoord]=2
                    win = checkwin(board,2)
                    stage=stage+1
        except ValueError:
            print("Vuelva a tirar")
            pass
    print(board)
    if win:
        print ("ganaste jugador 2")
        break