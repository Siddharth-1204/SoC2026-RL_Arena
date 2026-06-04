import pygame
import sys
from constants import *
from player import Player
from game import Game
from renderer import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RL Arena")
clock = pygame.time.Clock()

player1 = Player(40, 20, RED, 1)
player2 = Player(40, 60, BLUE, 2)

game = Game(ROWS, COLS)
game.add_player(player1)
game.add_player(player2)

actions_wasd = {pygame.K_a: (0, -1), pygame.K_w: (-1, 0),
                pygame.K_d: (0, 1), pygame.K_s: (1, 0)}
actions_arrows = {pygame.K_LEFT: (0, -1), pygame.K_RIGHT: (0, 1),
                  pygame.K_DOWN: (1, 0), pygame.K_UP: (-1, 0)}

running = True
game_over = False

while running:
    clock.tick(FPS)

    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Read keyboard, update player directions
    keys = pygame.key.get_pressed()
    for key in actions_wasd:
        if keys[key]:
            player1.dir = actions_wasd[key]
    for key in actions_arrows:
        if keys[key]:
            player2.dir = actions_arrows[key]
    if game_over:
        if keys[pygame.K_r] and not player1.alive:
            player1.reset()
            game_over=False
        if keys[pygame.K_SPACE] and not player2.alive:
            player2.reset()
            game_over=False
    # Call game.update()
    game.update()
    # If anyone died, change game_over var
    if not(player1.alive and player2.alive):
        game_over = True; 
    # Draw everything
    draw_grid(screen)
    for player in game.players:
        draw_trail(screen, player)
        draw_player(screen, player)
    # If game over, render text on top
    score_text = game.score()
    render_text(screen, score_text)
    pygame.display.update()

pygame.quit()