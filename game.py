import pygame

pygame.init()

# Constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
SQUARE_SIZE = SCREEN_WIDTH // 32 
GRID_SIZE = 32  
BOARD = [[0 for _ in range(32)] for _ in range(32)]
DIRECTION = ''
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

BOARD[2][2] = 2
# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the grid of squares
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            square_rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            if BOARD[x][y] == 0:
                pygame.draw.rect(screen, BLACK, square_rect)
            elif BOARD[x][y] == 1:
                pygame.draw.rect(screen, GREEN, square_rect)
            elif BOARD[x][y] == 2:
                pygame.draw.rect(screen, RED, square_rect)


    pygame.display.flip()

# Quit Pygame
pygame.quit()
