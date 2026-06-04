import pygame
from constants import *

def draw_grid(screen):
    screen.fill((255, 255, 255))
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (WIDTH, y))

def draw_player(screen, player):
    if not player.alive: return
    rect = pygame.Rect(player.pos[1]*CELL_SIZE, player.pos[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, player.color, rect, 2)

def draw_trail(screen, player):
    if not player.alive: return
    for pos in player.trail:
        if pos!=player.pos:
            rect = pygame.Rect(pos[1]*CELL_SIZE, pos[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, player.color, rect)    

def render_text(screen, text):
    font = pygame.font.Font(None, 80)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (200, 300))