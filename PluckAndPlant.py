import random

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
while(True):
    flower = [random.randint(0, 4), random.randint(0, 4)]
    if flower == [0,0]:
        continue
    else:
        break
    
bobby = [0,0]

hasFlower = False

board[flower[0]][flower[1]] = '*'
board[bobby[0]][bobby[1]] = '!'

def printBoard():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print("")

def testFlower():
    if bobby == flower:
        hasFlower = True
        print("Bobby now has the flower and can now plant it.")    

printBoard()
print("The flower is at: " + str(flower))
print("Bobby is at: " + str(bobby))

print("1. Hop left one.")
print("2. Hop up one.")
print("3. Hop right one.")
print("4. Hop down one.")
print("5. Plant/try to plant flower.")

while(True):
    userInput = int(input("Please input your choice(1-5): "))
    if userInput > 5 or userInput < 1:
        print("Out of range input. Try again.")
        continue
    
    if userInput == 1:
        if bobby[1] - 1 < 0:
            print("Cannot go this way, edge of board. Try again.")
            printBoard()
            continue
        board[bobby[0]][bobby[1]] = 0
        bobby = [bobby[0], bobby[1] - 1]
        board[bobby[0]][bobby[1]] = '!'
        testFlower()
        printBoard()
        continue
        
    if userInput == 2:
        if bobby[0] - 1 < 0:
            print("Cannot go this way, edge of board. Try again.")
            printBoard()
            continue
        board[bobby[0]][bobby[1]] = 0
        bobby = [bobby[0] - 1, bobby[1]]
        board[bobby[0]][bobby[1]] = '!'
        testFlower()
        printBoard()
        continue
        
    if userInput == 3:
        if bobby[1] + 1 > 4:
            print("Cannot go this way, edge of board. Try again.")
            printBoard()
            continue
        board[bobby[0]][bobby[1]] = 0
        bobby = [bobby[0], bobby[1] + 1]
        board[bobby[0]][bobby[1]] = '!'
        testFlower()
        printBoard()
        continue
        
    if userInput == 4:
        if bobby[0] + 1 > 4:
            print("Cannot go this way, edge of board. Try again.")
            printBoard()
            continue
        board[bobby[0]][bobby[1]] = 0
        bobby = [bobby[0] + 1, bobby[1]]
        board[bobby[0]][bobby[1]] = '!'
        testFlower()
        printBoard()
        continue
        
    if userInput == 5:
        if hasFlower == False:
            print("Bobby does not have the flower and thus cannot plant it.")
            continue
        else:
            flower = bobby
            board[flower[0]][flower[1]] = '*'
            continue     
