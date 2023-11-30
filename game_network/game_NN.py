import pygame
import constants as c
import snake as s
import random
from keras.models import load_model
import numpy as np



network = load_model("NN.keras")
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




# Main loop
running = True
while running:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    X = np.array(Board)
    X = X.flatten()
    X = X.reshape(1,400)

    prediction = network.predict(X)
    decision = np.argmax(prediction)

    turn = ''
    if decision == 0:
        turn = 'N'
    elif decision == 1:
        turn = 'E'
    elif decision == 2:
        turn = 'S'
    elif decision == 3:
        turn = 'W'
    
    snake.turn(turn)


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
    Board[foodx][foody] = 2

    for x in range(len(Board)):
        for y in range(len(Board[x])):
            square_rect = pygame.Rect(x * c.SQUARE_SIZE, y * c.SQUARE_SIZE, c.SQUARE_SIZE, c.SQUARE_SIZE)
            if Board[x][y] == 0:
                pygame.draw.rect(screen, c.BLACK, square_rect)
            elif Board[x][y] == 1:
                pygame.draw.rect(screen, (255,102,178), square_rect)
            elif Board[x][y] == 2:
                pygame.draw.rect(screen, (153,204,255), square_rect)
    
    pygame.display.flip()

    pygame.time.delay(200)

    
        
    
    




# Quit Pygame
pygame.quit()
