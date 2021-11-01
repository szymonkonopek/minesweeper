import os
import random
import keyboard
import time

ylen = 5
ylen = int(input("wysokosc / szerokosc planszy"))
xlen = ylen


arrowX = 0
arrowY = 0

num_of_placed_bombs = 0
#bombs = 2

bombs = int(input("Liczba bomb"))

delay = 0.1

mainArray = [[0 for x in range(ylen)] for y in range(ylen)]
bombArray = [["■" for x in range(ylen)] for y in range(ylen)]
arrowArray = [[0 for x in range(ylen)] for y in range(ylen)]
arrowArray[arrowX][arrowY] = 1 #startting pos for brackets

def displayArray():
    os.system("cls")
    for y in range(ylen): 
        row = []
        for x in range(xlen):
            if (bombArray[x][y] != "■" and bombArray[x][y] != "◎") or mainArray[x][y] == "□":
                if arrowArray[x][y] == 1:
                    row.append("[" + str(mainArray[x][y]) + "]")
                else:
                    row.append(" " + str(mainArray[x][y]) + " ")
            else:
                if arrowArray[x][y] == 1:
                    row.append("["+bombArray[x][y]+"]")
                else:
                    row.append(" "+ bombArray[x][y]+" ")
        print(" ".join(row))
        row = []

def placeBombs(num):
    for i in range(num):
        x = random.randint(0,xlen-1)
        y = random.randint(0,ylen-1)

        if mainArray[x][y] != "◍":
            mainArray[x][y] = "◍"
            cornerX = x-1
            cornerY = y-1
            for i in range(3):
                for j in range(3):
                    if cornerX+i >= 0 and cornerX+i <= xlen-1 and cornerY+j >=0 and cornerY+j <=ylen-1 and (cornerX+i != x or cornerY+j != y) and (mainArray[cornerX+i][cornerY+j] != "◍"):
                        mainArray[cornerX+i][cornerY+j] += 1
                        
        else:
            placeBombs(1)

def moveArrow(x,y):
    arrowArray[arrowX][arrowY] = 0
    arrowArray[arrowX+x][arrowY+y] = 1 

def placeBlanks(x,y):
    cornerX = x-1
    cornerY = y-1
    numbers = [1,2,3,4,5,6,7,8,9]
    for i in range(3):
                for j in range(3):
                    if cornerX+i >= 0 and cornerX+i <= xlen-1 and cornerY+j >=0 and cornerY+j <=ylen-1:
                        if mainArray[cornerX+i][cornerY + j] == 0:
                            mainArray[cornerX+i][cornerY+j] = "□"
                            placeBlanks(cornerX+i,cornerY+j)
                        elif mainArray[cornerX + i][cornerY +j] in numbers:
                            bombArray[cornerX+i][cornerY+j] = "?"
                        

def arrowsMove(x,y,num_of_placed_bombs):
    if keyboard.is_pressed("down"):
        if arrowY+1 <= ylen-1:
            start = moveArrow(0,1)
            y += 1
    elif keyboard.is_pressed("up"):
        if arrowY-1 >= 0:
            start = moveArrow(0,-1)
            y -= 1
    elif keyboard.is_pressed("left"):
        if arrowX-1 >= 0:
            start = moveArrow(-1,0)
            x -= 1
    elif keyboard.is_pressed("right"):
        if arrowX+1 <= xlen-1:
            start = moveArrow(1,0)
            x += 1
    elif keyboard.is_pressed("b"):
        if bombArray[x][y] == "■":
            bombArray[x][y] = "◎"
            if mainArray[x][y] == "◍":
                num_of_placed_bombs += 1
        elif bombArray[x][y] =="◎":
            bombArray[x][y] = "■"
            if mainArray[x][y] == "◍":
                num_of_placed_bombs -= 1
    elif keyboard.is_pressed("space"):
        if bombArray[x][y] == "◎":
            bombArray[x][y] = "■"
        elif mainArray[x][y] == "◍":
            print("end")
            input("")
            exit()
        else:
            bombArray[x][y] = "?"
            if mainArray[x][y] == 0:
                mainArray[x][y] = "□"
                placeBlanks(x,y)
    
    time.sleep(delay)
    displayArray()
    print("x " + str(arrowX))
    print("y " + str(arrowY))

    cords = [x,y, num_of_placed_bombs]
    return cords



placeBombs(bombs)

displayArray()



while 1:
    print(mainArray)
    if num_of_placed_bombs < bombs:
        cords = arrowsMove(arrowX,arrowY,num_of_placed_bombs)
        arrowX = cords[0]
        arrowY = cords[1]
        num_of_placed_bombs = cords[2]
        
    else:
        print("you won")
        exit()