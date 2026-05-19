from constants import *
from utils import *

# Create empty grid

grid = []

for _ in range(ROWS):
    row = [EMPTY_CELL] * COLS
    grid.append(row)


# Player starting position
player_row = 5
player_col = 5


# Obstacles
obstacles = [ ]

running = True

while running:

    # Reset grid

    # Add obstacles

    # Add player

    # Take input and update position

    # Boundary checking

    # Obstacle collision
    if (new_row, new_col) in obstacles:
        print("Invalid Move: Obstacle")
        continue

    player_row = new_row
    player_col = new_col
