import pygame
from pygame.locals import *
import time
import constants as c
import snake as s
import random

f = open("states.txt", 'a')
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
    dir = -1
    if snake.dir == 'N':
        dir = 0
    elif snake.dir == 'E':
        dir = 1
    elif snake.dir == 'S':
        dir = 2
    else:
        dir = 3

    f.write(str(dir) + "\n")
    

# Main loop
running = True
while running:

    directionCHanged = False

    saveState()

    # Detect user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN and not directionCHanged:
            if event.key == K_UP:
                snake.turn('N')
                directionCHanged = True
            if event.key == K_DOWN:
                snake.turn('S')
                directionCHanged = True
            if event.key == K_LEFT:
                snake.turn('W')
                directionCHanged = True
            if event.key == K_RIGHT:
                snake.turn('E')
                directionCHanged = True
    
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

    pygame.time.delay(200)

    
        
    
    




# Quit Pygame
pygame.quit()
