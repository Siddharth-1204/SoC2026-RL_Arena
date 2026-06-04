from constants import *
from utils import *
import numpy as np
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
change_obstacles = True
running = True

while running:

    # Reset grid
    new_grid = [row.copy() for row in grid]
    # Add obstacles
    if change_obstacles:
        obstacles = np.random.randint(low=0, high=10, size=(10, 2))
    for i in range(10):
        new_grid[obstacles[i][0]][obstacles[i][1]]=OBSTACLE_CELL
    # Add player
    new_grid[player_row-1][player_col-1]=PLAYER_CELL
    print_grid(new_grid)
    # Take input and update position
    move = input("Enter your move (W,A,S,D):")
    match move:
            case "W"|"w":
                new_row, new_col = player_row-1, player_col
            case "D"|"d":
                new_row, new_col = player_row, player_col+1
            case "S"|"s":
                new_row, new_col = player_row+1, player_col
            case "A"|"a":
                new_row, new_col = player_row, player_col-1
            case _:
                print("Invalid Move, choose from W,A,S,D")
                change_obstacles = False
                continue
    # Boundary checking
    if new_row<1 or new_row>10 or new_col<1 or new_col>10:
        print("Invalid Move: Boundary")
        change_obstacles = False
        continue
    # Obstacle collision
    if new_grid[new_row-1][new_col-1] == OBSTACLE_CELL:
        print("Invalid Move: Obstacle")
        change_obstacles = False
        continue
    change_obstacles = True
    player_row = new_row
    player_col = new_col
