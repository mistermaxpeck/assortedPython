# Conway's Game of Life

import random, time, copy

WIDTH = 79
HEIGHT = 20

ALIVE = '#'
DEAD = ' '

#create list of list for cells

print('''CONWAY\'S GAME OF LIFE

Press enter to start.''')
startGame = input()

nextCells = []
for x in range(WIDTH):
    column= [] #create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append(ALIVE) #add living cell
        else:
            column.append(DEAD) #add dead cell
    nextCells.append(column)

while True:
    print('\n\n\n\n\n') #seperate each step with newline
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()
    print('''
    Press CTRL-C to quit.''')
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord]==ALIVE:
                numNeighbors+=1
            if currentCells[x][aboveCoord]==ALIVE:
                numNeighbors+=1
            if currentCells[rightCoord][aboveCoord]==ALIVE:
                numNeighbors+=1
            if currentCells[leftCoord][y]==ALIVE:
                numNeighbors+=1
            if currentCells[rightCoord][y]==ALIVE:
                numNeighbors+=1
            if currentCells[leftCoord][belowCoord]==ALIVE:
                numNeighbors+=1
            if currentCells[x][belowCoord]==ALIVE:
                numNeighbors+=1
            if currentCells[rightCoord][belowCoord]==ALIVE:
                numNeighbors+=1

            if currentCells[x][y]== ALIVE and (numNeighbors==2 or numNeighbors==3):
                nextCells[x][y]=ALIVE
            elif currentCells[x][y]==DEAD and numNeighbors==3:
                nextCells[x][y]=ALIVE
            else:
                nextCells[x][y]=DEAD
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print('Thanks for playing!')
        sys.exit()
