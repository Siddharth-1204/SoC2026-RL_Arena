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
        self.in_territory = True
        self.territory_generate()

    def reset(self):
        self.pos = self.start_pos
        self.dir = self.start_dir
        self.trail = []
        self.alive = True
        self.in_territory = True
        self.territory_generate()

    def territory_generate(self):
        self.territory = []
        for i in range(self.start_pos[0]-2, self.start_pos[0]+3):
            for j in range(self.start_pos[1]-2, self.start_pos[1]+3):
                self.territory.append((i, j))