import pygame
from constants import *
from player import Player
from game import Game
from renderer import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RL Arena")
clock = pygame.time.Clock()

player1 = Player(5, 5, RED)
player2 = Player(15, 15, BLUE)

game = Game(ROWS, COLS)
game.add_player(player1)
game.add_player(player2)

actions_wasd = {pygame.K_w: (0, -1), pygame.K_a: (-1, 0),
                pygame.K_s: (0, 1), pygame.K_d: (1, 0)}
actions_arrows = {pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1),
                  pygame.K_RIGHT: (1, 0), pygame.K_LEFT: (-1, 0)}

running = True
game_over = False

while running:
    clock.tick(FPS)

    # Handle quit event
    # Read keyboard, update player directions
    # Call game.update()
    # If anyone died, change game_over var
    
    # Draw everything
    # If game over, render text on top
    pygame.display.update()

pygame.quit()