from constants import *
from capture import *
import numpy as np

class Game:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.trail_grid = np.zeros((rows, cols), dtype=int)
        self.territory_grid = np.zeros((rows, cols), dtype=int)
        self.helper_grid = self.territory_grid.copy()
        self.players = []

    def add_player(self,player):
        self.players.append(player)
        for pos in player.territory:
            self.territory_grid[pos[0]][pos[1]] = player.number

    def update(self):
        # compute all next positions(if the player is trying to move out of bounds then he is blocked)
        for player in self.players:
            player.next_pos=(player.pos[0]+player.dir[0], player.pos[1]+player.dir[1])
            if player.next_pos[0]<0 or player.next_pos[0]>=self.rows or player.next_pos[1]<0 or player.next_pos[1]>=self.cols:
                player.next_pos = player.pos
        # head-on — same target cell kills both
        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                if self.players[i].next_pos == self.players[j].next_pos:
                    self.players[i].alive = False
                    self.players[j].alive = False
        # if the player is killing anyone by entering their trail or killing himself by entering his trail:
        for player in self.players:
            if self.trail_grid[player.next_pos[0]][player.next_pos[1]]!=0:
                dead_player = self.get_player(self.trail_grid[player.next_pos[0]][player.next_pos[1]])
                dead_player.alive = False
        # if the player is entering other's current_pos(which is going to become their trail):
        for i in range(len(self.players)):
            for j in range(len(self.players)):
                if self.players[i].next_pos == self.players[j].pos and self.players[i].next_pos != self.players[j].next_pos:
                    self.players[j].alive = False
        # after finally deciding who will live and who will die, we should remove data of dead players
        for player in self.players:
            if not player.alive:
                for pos in player.trail:
                    self.trail_grid[pos[0]][pos[1]]=0
                for pos in player.territory:
                    self.territory_grid[pos[0]][pos[1]]=0
                player.trail = []
                player.territory = []
                self.players.remove(player)
        # move the players who survived
        for player in self.players:
            if player.alive:
                # if increasing his trail
                if player.in_territory == False and self.territory_grid[player.next_pos[0]][player.next_pos[1]] != player.number:
                    if player.pos != player.next_pos:
                        player.trail.append(player.pos)
                        self.trail_grid[player.pos[0]][player.pos[1]]=player.number
                    player.pos=player.next_pos
                # if moving in his territory
                elif player.in_territory and self.territory_grid[player.next_pos[0]][player.next_pos[1]] == player.number:
                    player.pos = player.next_pos
                # if moving out from his territory
                elif player.in_territory and self.territory_grid[player.next_pos[0]][player.next_pos[1]] != player.number:
                    player.in_territory = False
                    player.pos = player.next_pos
                # if entering his territory 
                else :
                    player.trail.append(player.pos)
                    self.trail_grid[player.pos[0]][player.pos[1]]=player.number
                    fill(self, player) # will just fill territory_grid including trail positions
                    for pos in player.trail:
                        self.trail_grid[pos[0]][pos[1]] = 0
                    player.trail = []
                    player.in_territory = True
                    player.pos = player.next_pos

    def reset(self):
        self.territory_grid.fill(0)
        self.trail_grid.fill(0)
        for player in self.players:
            player.reset()

    def score(self):
        score_text=""
        for player in self.players:
            score_text+=f" {player.number} : {len(player.territory)} "
        return score_text
    
    def get_player(self, number):
        for player in self.players:
            if player.number==number:
                return player