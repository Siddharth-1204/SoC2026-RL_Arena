import pygame
import numpy as np
from constants import *

def draw_grid(screen, game):
    screen.fill((255, 255, 255))
    grid_surf = pygame.Surface((WIDTH, HEIGHT))
    grid_rect = pygame.Surface.get_rect(grid_surf, topleft = (0, EXTRA_HEIGHT))
    colors_array = np.full((WIDTH, HEIGHT, 3), 255)
    
    for player in game.players:
        for terr_pos in player.territory:
            for i in range(CELL_SIZE):
                for j in range(CELL_SIZE):
                    colors_array[terr_pos[1]*CELL_SIZE+j][terr_pos[0]*CELL_SIZE+i] = (player.color[0]/2, player.color[1]/2, player.color[2]/2)
    for player in game.players:
        for trail_pos in player.trail:
            for i in range(CELL_SIZE):
                for j in range(CELL_SIZE):
                    colors_array[trail_pos[1]*CELL_SIZE+j][trail_pos[0]*CELL_SIZE+i] = player.color
    
    for j in range(0, HEIGHT):
        for i in range(0, WIDTH, CELL_SIZE):
            colors_array[i][j] = GRAY
        for i in range(CELL_SIZE-1, WIDTH, CELL_SIZE):
            colors_array[i][j] = GRAY
    
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT, CELL_SIZE):
            colors_array[i][j] = GRAY
        for j in range(CELL_SIZE-1, HEIGHT, CELL_SIZE):
            colors_array[i][j] = GRAY

    pygame.surfarray.blit_array(grid_surf, colors_array)

    for player in game.players:
        pygame.draw.circle(grid_surf, GRAY, (CELL_SIZE*player.pos[1]+CELL_SIZE/2, CELL_SIZE*player.pos[0]+CELL_SIZE/2), CELL_SIZE/2-2)
        pygame.draw.circle(grid_surf, player.color, (CELL_SIZE*player.pos[1]+CELL_SIZE/2, CELL_SIZE*player.pos[0]+CELL_SIZE/2), CELL_SIZE/2-3)

    screen.blit(grid_surf, grid_rect)

def render_text(screen, text):
    font = pygame.font.Font(None, 80)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (250, 50))