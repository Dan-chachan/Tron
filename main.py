import pygame
from setup import *
from random import randint
from setup import *

pygame.init()
pygame.display.set_caption("TRON")
pygame.font.init()
font = pygame.font.SysFont("Consolas", 20, True)


def draw_car(color, x, y, size=GRID_SIZE):
    pygame.draw.rect(screen, color, 
        (x, y, size, size))

def draw_pause():
    pause_x = 30
    pause_y = 30
    pause_wid = 10
    pause_hei = 35
    pause_col = RED

    pygame.draw.rect(screen, pause_col,
        (pause_x, pause_y, pause_wid, pause_hei))
    
    pygame.draw.rect(screen, pause_col,
        ((pause_x + 2 * pause_wid), pause_y, pause_wid, pause_hei))

while not done:
    # User did something
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = (not pause) # If paused: unpause
            # Directions
            elif event.key == pygame.K_UP:
                dir1 = 'U'
            elif event.key == pygame.K_DOWN:
                dir1 = 'D'
            elif event.key == pygame.K_LEFT:
                dir1 = 'L'
            elif event.key == pygame.K_RIGHT:
                dir1 = 'R'
            elif event.key == pygame.K_s:
                dir2 = 'D'
            elif event.key == pygame.K_a:
                dir2 = 'L'
            elif event.key == pygame.K_d:
                dir2 = 'R'
            elif event.key == pygame.K_w:
                dir2 = 'U'
    
    # Reset the screen
    screen.fill(T_DARK)
    #
    # Executive code here
    
    draw_car(T_ORANGE, 500, 30)

    if not pause:
        pygame.draw.rect(screen, T_ORANGE, (30, 30, 10, 10))

    else:
        draw_pause()

    #
    # Show the new content and wait
    pygame.display.flip()
    clock.tick(60)