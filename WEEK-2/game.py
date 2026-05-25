from constants import *
import numpy as np

class Game:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)
        self.players = []

    def add_player(self,player):
        pass

    def update(self):
        # compute all next positions
        # head-on — same target cell kills both
        # move the players who survived
        pass

    def reset(self):
        pass