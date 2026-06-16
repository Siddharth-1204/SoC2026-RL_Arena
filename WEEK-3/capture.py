def fill(game, player):
    game.helper_grid = game.territory_grid.copy()
    for row in range(game.rows):
        bfs(game, row, 0, player.number)
        bfs(game, row, game.cols-1, player.number)
    for col in range(game.cols):
        bfs(game, game.rows-1, col, player.number)
        bfs(game, 0, col, player.number)
    for row in range(game.rows):
        for col in range(game.cols):
            if game.helper_grid[row][col]!=player.number:
                if game.territory_grid[row][col]!=0:
                    player2 = game.get_player(game.territory_grid[row][col])
                    player2.territory.remove((row, col))
                game.territory_grid[row][col]=player.number
                player.territory.append((row, col))
    game.helper_grid = game.territory_grid.copy()
    return
    

def bfs(game, row, col, n):
    if row<0 or row>=game.rows or col<0 or col>=game.cols or game.helper_grid[row][col]==n or game.trail_grid[row][col]==n:
        return
    game.helper_grid[row][col]=n
    bfs(game, row+1, col, n)
    bfs(game, row-1, col, n)
    bfs(game, row, col+1, n)
    bfs(game, row, col-1, n)
    return