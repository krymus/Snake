import pygame
from pygame.locals import *
import time
import constants as c



pygame.init()

# Create a window
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

Board = []
for x in range(c.GRID_SIZE):
        row = []
        for y in range(c.GRID_SIZE):
            square = pygame.Rect(x * c.SQUARE_SIZE, y * c.SQUARE_SIZE, c.SQUARE_SIZE, c.SQUARE_SIZE)
            pygame.draw.rect(screen, c.BLACK, square)
            row.append(square)
        Board.append(row)

Direction = ''
Snake = []
size = -1

# starting positon
Snake.append([11,15])
Snake.append([12,15])
Snake.append([13,15])
Snake.append([14,15])
size = len(size)
Direction = 'E'

# draw snake
for x in Snake:
    pygame.draw.rect(screen, c.WHITE, Board[x[0]][x[1]])



def moveSnake():
    pygame.draw.rect(screen, c.WHITE, Board[Snake[-1][0]][Snake[-1][1]])
    for i in range(len(Snake)-1, 0, -1):
        Snake[i] = Snake[i-1]

    if Direction == 'N':
        Snake.append([Snake[0][0], (Snake[0][1] -1]])
    elif Direction == 'S':
        Snake.append([Snake[0][0], (Snake[0][1] + 1)%c.GRID_SIZE])







# Main loop
running = True
while running:
    # Detect user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                if not Direction == 'S':
                    Direction = 'N'
            if event.key == K_DOWN:
                if not Direction == 'N':
                    Direction = 'S'
            if event.key == K_LEFT:
                if not Direction == 'E':
                    Direction = 'W'
            if event.key == K_RIGHT:
                if not Direction == 'W':
                    Direction = 'E'
         

 
    # Draw the grid of squares
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            square_rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            if Board[x][y] == 0:
                pygame.draw.rect(screen, BLACK, square_rect)
            elif Board[x][y] == 1:
                pygame.draw.rect(screen, GREEN, square_rect)
            elif Board[x][y] == 2:
                pygame.draw.rect(screen, RED, square_rect)
    
    time.sleep(1)

    





    pygame.display.flip()

# Quit Pygame
pygame.quit()
