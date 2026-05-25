# Week 2 - Pygame
Modify the previous week's assignment by adding Pygame logic with two players.
Two players move around leaving trails behind them. If you hit a trail, or crash head-on into the other player : you die.

## RESOURCES
### Pygame Tutorials

- [Option 1](https://www.youtube.com/watch?v=AY9MnQ4x3zk)
- [Option 2](https://www.youtube.com/watch?v=QFvqStqPCRU)
- [Option 3](https://realpython.com/pygame-a-primer)

### Installations:
- Python 3
- `pygame` (`pip install pygame`)
- `numpy` (`pip install numpy`)

(You may need to use a virtual environment. Feel free to ask if you face any issues.)

## Assignment

### Directory Structure

```
WEEK-2/
├── constants.py    — game settings (screen size, colors, etc.)
├── player.py       — Player class
├── game.py         — Game class (collision, movement logic)
├── renderer.py     — drawing functions (grid, players, trails)
├── main.py         — game loop (put it all together)
```

### 1. `constants.py`

Store all your numbers and colors here so they're easy to tweak.

- Screen size (800 x 800), grid size (80 x 80)
- Cell size = screen width ÷ columns
- FPS (start with 10 — it's slow enough to see what's happening)
- Colors as RGB tuples (WHITE, BLACK, RED, BLUE, GRAY)

### 2. `player.py`

Create a `Player` class.

A player should store:
- current position
- direction
- trail information
- color
- alive/dead state

Also support resetting the player back to its initial state.


### 3. `game.py`

This class manages the full game state.

**`__init__(self, rows, cols)`**
- Create the game grid
- Store all players

**`add_player(self, player)`**
- Add players to the game
- Track them inside the grid

**`update(self)`**
This runs every frame.

Handle:
1. Computing next positions
2. Player movement
3. Collision checking
4. Trail updates

Players should:
- die on wall collisions
- die on trail collisions
- die on head-on collisions

> Think carefully about update order.  
> All players should effectively move at the same time.

> Use the numpy grid for collision checks. 
> `self.grid[next_pos] != 0` is way faster than `next_pos in player.trail`.  
> With 80×80 cells and long trails, the list check gets slow.
**`reset(self)`**
- Clear the game state
- Reset all players
- Restore starting positions


### 4. `renderer.py`

Create drawing functions for:
- the grid
- players
- trails

You may create additional helper functions if needed.


### 5. `main.py`

This is the game loop.

## Try to implement these too (Optional)

- Add a score system (cells occupied by a player)
- Let players restart with a key press (R or SPACE)
- Make trails fade out over time instead of staying forever

## Peeeking into Week-3
- Next week, you’ll implement the Flood Fill Algorithm.
- There are multiple ways to solve Flood Fill, but we’ll primarily explore BFS and DFS based implementations as they are easier to understand and implement.
- Efficient approach is Scanline algorithm, but it can be slightly harder for first-time learners.
- Try learning the algorithm before next week. (You can implement in any way you like)


## ❗️ Note

> Try to solve things on your own first, and especially focus on learning how to debug without any help.
> It is highly recommended that you share your doubts, approaches, progress, and problems related to the questions and/or content in the **WhatsApp group**.
