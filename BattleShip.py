import random

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
ship1 = [random.randint(0, 4), random.randint(0, 4)]

goodToGo = True
shipCount = 0
while(goodToGo):
    ship1 = [random.randint(0, 4), random.randint(0, 4)]
    ship2 = [random.randint(0, 4), random.randint(0, 4)]
    ship3 = [random.randint(0, 4), random.randint(0, 4)]
    ship4 = [random.randint(0, 4), random.randint(0, 4)]
    if ship1 != ship2 != ship3 != ship4:
        goodToGo = False

board[ship1[0]][ship1[1]] = '*'
board[ship2[0]][ship2[1]] = '*'
board[ship3[0]][ship3[1]] = '*'
board[ship4[0]][ship4[1]] = '*'

sunkShip = 0
count = 0
while(count != 4):
    userRow = int(input("Please input row number you guess (0-4): "))
    if userRow > 4 or userRow < 0:
        print("Out of range input. Try again.")
        continue
    
    userCol = int(input("Please input column number you guess (0-4): "))
    if userCol > 4 or userCol < 0:
        print("Out of range input. Try again.")
        continue
    
    if board[userRow][userCol] == '*':
        print("HIT!")
        sunkShip += 1
    else:
        print("MISS!")
    count += 1

if sunkShip != 4:
    print("YOU LOOSE!")
else:
    print("YOU WIN!")
    