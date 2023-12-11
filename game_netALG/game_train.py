import pygame
from pygame.locals import *
import time
import constants as c
import snake as s
import random

f = open("game_netALG/statesALG.txt", 'a')

pygame.init()

# Create a window
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

Board = [[0 for _ in range(c.GRID_SIZE)] for i in range(c.GRID_SIZE)]
snake = s.Snake()

for x in snake.body:
        Board[x[0]][x[1]] = 1

foodx = -1
foody = -1

def foodDraw():
    global foodx, foody
    x = random.randint(0, c.GRID_SIZE-1)
    y = random.randint(0, c.GRID_SIZE-1)
    while not Board[x][y] == 0:
        x = random.randint(0, c.GRID_SIZE-1)
        y = random.randint(0, c.GRID_SIZE-1)
    foodx = x
    foody = y

foodDraw()

def saveState():
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            if snake.head == [i,j]:
                f.write("2")
            else:
                f.write(str(Board[i][j]))
    f.write(" ")

def saveDecision():
    f.write(str(snake.dir) + "\n")


def distance(x1, y1, x2, y2):
    distX = abs(x1 - x2)
    distY = abs(y1 - y2)
    return distX + distY
       

def decision():
    
    x = snake.head[0] 
    y = snake.head[1] 

    if (y > foody) and not Board[x][(y-1)%20] == 1:
        return 0
    elif foody > y and not Board[x][(y+1)%20] == 1:
        return 2
    elif x > foodx and not Board[(x-1)%20][y] == 1:
        return 3
    elif x < foodx and not Board[(x+1)%20][y] == 1:
        return 1
    else:
        if Board[x][(y+1)%20] == 0:
            return 2
        elif Board[x][(y-1)%20] == 0:
            return 0
        elif Board[(x+1)%20][y] == 0:
            return 1
        elif Board[(x-1)%20][y] == 0:
            return 3
    
    return random.randint(0,3)
 


# Main loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    saveState()

    snake.turn(decision())
    
    saveDecision()

    if snake.head[0] == foodx and snake.head[1] == foody: 
        foodDraw()
        snake.move(True)
    else:
        snake.move(False)

    if Board[snake.head[0]][snake.head[1]] == 1:
        running = False

    # Update board
    Board = [[0 for _ in range(c.GRID_SIZE)] for _ in range(c.GRID_SIZE)]
    for x in snake.body:
        Board[x[0]][x[1]] = 1
    Board[foodx][foody] = 8

    for x in range(len(Board)):
        for y in range(len(Board[x])):
            square_rect = pygame.Rect(x * c.SQUARE_SIZE, y * c.SQUARE_SIZE, c.SQUARE_SIZE, c.SQUARE_SIZE)
            if Board[x][y] == 0:
                pygame.draw.rect(screen, c.BLACK, square_rect)
            elif Board[x][y] == 1:
                pygame.draw.rect(screen, (255,102,178), square_rect)
            elif Board[x][y] == 8:
                pygame.draw.rect(screen, (153,204,255), square_rect)
    
    pygame.display.flip()

    pygame.time.delay(1)

# Quit Pygame
pygame.quit()
