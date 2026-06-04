from constants import *
import numpy as np

class Game:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)
        self.players = []

    def add_player(self,player):
        self.players.append(player)
        self.grid[player.start_pos[0]][player.start_pos[1]]=player.number

    def update(self):
        # compute all next positions
        for player in self.players:
            player.next_pos=(player.pos[0]+player.dir[0], player.pos[1]+player.dir[1])
        # head-on — same target cell kills both
        for player in self.players:
            if player.next_pos[0]<0 or player.next_pos[0]>=self.rows or player.next_pos[1]<0 or player.next_pos[1]>=self.cols:
                player.alive=False
            elif self.grid[player.next_pos[0]][player.next_pos[1]] != 0:
                player.alive=False
        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                if self.players[i].next_pos == self.players[j].next_pos:
                    self.players[i].alive = False
                    self.players[j].alive = False
        for player in self.players:
            if not player.alive:
                for pos in player.trail:
                    self.grid[pos[0]][pos[1]]=0
        # move the players who survived
        for player in self.players:
            if player.alive:
                player.pos=player.next_pos
                player.trail.append(player.pos)
                self.grid[player.pos[0]][player.pos[1]]=player.number

    def reset(self):
        self.grid.fill(0)
        for player in self.players:
            player.reset()
            self.grid[player.start_pos[0]][player.start_pos[1]]=player.number
            player.trail.append(player.start_pos)

    def score(self):
        score_text=""
        for player in self.players:
            score_text+=f" {player.number} : {len(player.trail)} "
        return score_text