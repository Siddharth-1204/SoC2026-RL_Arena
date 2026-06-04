class Player:
    def __init__(self, row, col, color, player_no):
        self.pos = (row, col)
        self.color = color
        self.dir = (1, 0)
        self.trail = []
        self.alive = True
        self.start_pos = (row, col)
        self.start_dir = (1,0)
        self.number = player_no
        self.trail.append(self.start_pos)

    def reset(self):
        self.pos = self.start_pos
        self.dir = self.start_dir
        self.trail = []
        self.alive = True
        self.trail.append(self.start_pos)