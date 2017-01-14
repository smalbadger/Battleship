import turtle
import random

window = turtle.Screen()
window.bgcolor("blue")

sam = turtle.Turtle()
sam.speed(0)

sam.shape("blank")
sam.pensize(2)
sam.color("black")
sam.up()
sam.goto(-430,-200)


##################### MAKE THE BOARD #######################
def printboard(board):
    for i in range(10):
        print(board[i][0], board[i][1], board[i][2], board[i][3], board[i][4], board[i][5], board[i][6], board[i][7], board[i][8],board[i][9])

def checkforvalidguess(layover, board, guess):
    alpha = guess[0].lower()
    tempnum0= ord("a")
    tempnum1= ord(alpha)
    num = tempnum1-tempnum0
    if layover[int(guess[1])-1][num]==0:
        layover[int(guess[1])-1][num] = board[int(guess[1])-1][num]
        if board[int(guess[1])-1][num]==0:
            layover[int(guess[1])-1][num]= "miss"
        return True
    else:
        return False

def drawguesses(layover, guesses, comporplayer):
    newguesses = guesses.copy()
    for i in range(len(guesses)):
        alpha = guesses[i][0].lower()
        tempnum0= ord("a")
        tempnum1= ord(alpha)
        num = tempnum1-tempnum0
        newguesses = guesses.copy()
        newguesses[i][0] = num
        newguesses[i][1] = int(newguesses[i][1])-1
    for j in range(len(guesses)):
        sam.setheading(0)
        sam.pensize(5)
        sam.up()
        if comporplayer == 0:
            sam.goto((-1 * (10 -  int(guesses[j][0])) * 40)-10, (10-int(guesses[j][1]))*40 - 220)
        else:
            sam.goto(50 + (int(guesses[j][0])*40), (10-int(guesses[j][1]))*40 - 220)
        if layover[int(guesses[j][1])][int(guesses[j][0])] == "miss":  
            sam.setheading(0)
            sam.color("white")                                                           
            O = 10
            sam.forward(O)
            sam.down()
            sam.left(90)
            sam.circle(O)
            sam.up()
        else:
            sam.color("red")
            sam.up()
            sam.setheading(135)
            sam.forward(20)
            sam.down()
            sam.forward(-40)
            sam.up()
            sam.forward(20)
            sam.right(90)
            sam.forward(20)
            sam.down()
            sam.forward(-40)
            sam.up()
            sam.forward(20)


def placeships(board, comporplayer):
    for shipnum in [5,4,3,3,2]:
        isvalid = 1
        endpos = 11
        direction = random.randrange(0,2)
        rowOrCol = random.randrange(0,10)
        while endpos > 10:
            startpos = random.randrange(0,10)
            endpos = startpos + shipnum

        for i in range(shipnum):
            if direction == 0:
                if board[rowOrCol][startpos + i] != 0:
                    isvalid = 0
            else:
                if board[startpos + i][rowOrCol] != 0:
                    isvalid = 0

        while isvalid == 0:
            isvalid = 1
            direction = random.randrange(0,2)
            rowOrCol = random.randrange(0,10)
            while endpos > 8:
                startpos = random.randrange(0,10)
                endpos = startpos + shipnum

            for i in range(shipnum):
                if direction == 0:
                    if board[rowOrCol][startpos + i] != 0:
                        isvalid = 0
                else:
                    if board[startpos + i][rowOrCol] != 0:
                        isvalid = 0

        #draw the ships
        sam.pensize(20)

        if comporplayer == 1 :
            sam.up()
            if direction == 0:
                sam.setheading(0)
            else:
                sam.setheading(270)

            if direction == 0:
                if comporplayer == 0:
                    sam.goto(-410+(40*startpos),180 - (40*rowOrCol))
                else:
                    sam.goto(50+(40*startpos),180 - (40*rowOrCol))
            else:
                if comporplayer == 0:
                    sam.goto(-410+(40*rowOrCol),180 - (40*startpos))
                else:
                    sam.goto(50+(40*rowOrCol),180 - (40*startpos))

            sam.down()
            sam.color("gray")
            sam.forward(40*(shipnum-1))

        if direction == 0:   #ship is going horizontal
            for i in range(shipnum):
                board[rowOrCol][startpos+i] = shipnum
        else:               #ship is going vertical
            for j in range(shipnum):
                board[startpos+j][rowOrCol] = shipnum

def checkforwinner(layover, player):
    sum = 0
    for i in range(10):
        for j in range(10):
            if layover[i][j] == "miss":
                sum = sum + 0
            else:
                sum = sum + layover[i][j]

    if sum == 63:
        return player
    else:
        return -1


def checkforsink(layover, shipssunklist):
    for i in range(10):
        for j in range(10):
            if layover[i][j] != "miss" and layover[i][j]!=0:
                vertsum = layover[i][j]
                horisum = layover[i][j]
                for k in range(1,layover[i][j]):
                    if i + k <=9:
                        if layover[i+k][j] != "miss":
                            vertsum = vertsum + layover[i+k][j]
                    if j + k <=9:
                        if layover[i][j+k] != "miss":
                            horisum = horisum + layover[i][j+k]
                if vertsum == layover[i][j]**2 or horisum == layover[i][j]**2:
                    if layover[i][j] not in shipssunklist:
                        shipssunklist.append(layover[i][j])
                        print("Ship of length ", layover[i][j], " has been sunk.", sep = "")

def computersturn(compturn):
    numshots = 5-len(compsinklist)
    print("\n\nCOMPUTER IS PLAYING\n\n")
    guesses = [["a",1],["a",1],["a",1],["a",1],["a",1]]
    while numshots < len(guesses):
        del guesses[-1]
    for k in range(1,numshots+1):
        columns = "abcdefghij"
        if compturn == 1:
            n = columns[random.randrange(0,10)]+str(random.randrange(1,11))
        else:
            ###########   STRATEGIC PLAY   #############
            n=0
            newcoord = [0,0]
            for i in range(10):
                for j in range(10):
                    if playlayover[i][j] != "miss" and playlayover[i][j] != 0:
                        if i<9:
                            if playlayover[i+1][j] == 0:
                                #newcoord = [i+1,j]
                                newcoord = [j,i+1]
                                break
                        elif i>1:
                            if playlayover[i-1][j] == 0:
                                #newcoord = [i-1,j]
                                newcoord = [j,i-1]
                                break
                        elif j<9:
                            if playlayover[i][j+1] == 0:
                                #newcoord = [i,j+1]
                                newcoord = [j+1,i]
                                break
                        elif j>1:
                            if playlayover[i][j-1] == 0:
                                #newcoord = [i,j-1]
                                newcoord = [j-1,i]
                                break

        if n != 0:
            if len(n) == 3 and n[0] in columns and n[1] == "1" and n[2] == "0":
                newcoord = [n[0], n[1]+n[2]]

            elif len(n)==2:
                newcoord=list(n)
        else:
            n = str(newcoord[0])+str(newcoord[1])
        while n[0] not in columns or not checkforvalidguess(playlayover, playersboard, newcoord) or len(n)!=2 or  n[1] not in rows:
            if len(n) == 3 and n[0] in columns and n[1] == "1" and n[2] == "0":
                newcoord = [n[0], n[1]+n[2]]
                break
            n = columns[random.randrange(0,10)]+str(random.randrange(0,10))
            if len(n)==2:
                newcoord=list(n)
        guesses[k-1]=newcoord
    print(guesses)
    drawguesses(playlayover, guesses, 1)
    checkforsink(playlayover, playsinklist)


#make horizontal lines for both boards
for i in range(11):
    sam.down()
    sam.forward(400)
    sam.up()
    sam.forward(60)
    sam.down()
    sam.forward(400)
    sam.up()
    sam.forward(-860)
    sam.left(90)
    sam.forward(40)
    sam.right(90)

#make verticle lines for both boards
sam.goto(-430,-200)
sam.left(90)
for i in range(11):
    sam.down()
    sam.forward(400)
    sam.up()
    sam.forward(-400)
    sam.right(90)
    sam.forward(40)
    sam.left(90)
sam.right(90)
sam.forward(20)
sam.left(90)
for i in range(11):
    sam.down()
    sam.forward(400)
    sam.up()
    sam.forward(-400)
    sam.right(90)
    sam.forward(40)
    sam.left(90)

#write column numbers
sam.goto(-400, 200)
sam.right(90)
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for alpha in letters:
    sam.write(alpha, align = "right", font = ("Arial",20,"normal"))
    sam.forward(40)
sam.forward(60)
for alpha in letters:
    sam.write(alpha, align = "right", font = ("Arial",20,"normal"))
    sam.forward(40)

#write row letters
sam.goto(-435,-195)
sam.left(90)
for num in range(1,11):
    sam.write(11-num, align = "right", font = ("Arial",20,"normal"))
    sam.forward(40)
sam.goto(25,-195)
for num in range(1,11):
    sam.write(11-num, align = "right", font = ("Arial",20,"normal"))
    sam.forward(40)

computersboard = [[0 for row in range(10)] for column in range(10)]
playersboard   = [[0 for row in range(10)] for column in range(10)]
complayover = [[0 for row in range(10)] for column in range(10)]
playlayover = [[0 for row in range(10)] for column in range(10)]

##################### PLACE THE SHIPS #######################

##################### PLACE THE SHIPS #######################

placeships(computersboard, 0)
placeships(playersboard, 1)

##################### PLAY THE GAME!!! #######################

#########DEBUGGING ONLY#############
#printboard(computersboard)
#print("\n\n\n",end = '')
#printboard(playersboard)

compsinklist = []
playsinklist = []
count = 0
winner = -1
while winner == -1:
    count = count+1
    numshots = 5 - len(playsinklist)
    print("Please enter", numshots, "coordinates: ")
    guesses = [["a",1],["a",1],["a",1],["a",1],["a",1]]

    while numshots < len(guesses):
        del guesses[-1]

    for i in range(1,numshots+1):
        columns = "ABCDEFGHIJabcdefghij"
        rows = "12345678910"
        newstr = str(i) + ". "
        n = input(newstr)

        while len(n)<2:
            n = input("Enter a valid coordinate: ")

        if len(n) == 3 and n[0] in columns and n[1] == "1" and n[2] == "0":
            newcoord = [n[0], n[1]+n[2]]

        if len(n)==2:
            newcoord=list(n)

        while n[0] not in columns or not checkforvalidguess(complayover, computersboard, newcoord) or len(n)!=2 or  n[1] not in rows:
            if len(n) == 3 and n[0] in columns and n[1] == "1" and n[2] == "0":
                newcoord = [n[0], n[1]+n[2]]
                break
            n = input("Enter a valid coordinate: ")
            while len(n)<2:
                n = input("Enter a valid coordinate: ")
            if len(n)==2:
                newcoord=list(n)
        guesses[i-1]=newcoord
    print(guesses)
    drawguesses(complayover, guesses, 0)
    checkforsink(complayover, compsinklist)
    
    winner = checkforwinner(complayover, 1)
    if winner != -1:
        break

    else:
        computersturn(count)

    winner = checkforwinner(playlayover, 0)
    if winner != -1:
        break

if winner == 1:
    print("\n")
    for i in range(10):
        print("You Win!!!")
elif winner == 0:
    print("You Lose :(")

print("\nPlease click anywhere on the board.")

window.exitonclick()