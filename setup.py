import pygame

# DEFAULT COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (74, 255, 54)
RED = (255, 33, 31)
BLUE = (59, 71, 255)
AQUA = (49, 225, 232)
PINK = (232, 42, 204)
ORANGE = (255, 85, 14)
YELLOW = (232, 194, 55)
DEEP_PURPLE = (35, 24, 46)
GREYISH_PURPLE = (61, 45, 64)

# TRON COLORS
T_ORANGE = (249, 163, 0)
T_BLUE = (1, 182, 199)
T_DARK = (4, 35, 44)
T_DARKBLUE = (2, 51, 66)


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)

GRID_SIZE = 5


# Loop until the user clicks the close button.
done = False

# Both players are alive
playing = True

# The game is paused
pause = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#############################################

