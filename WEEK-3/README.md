# Week 3

This week, extend your Week 2 by adding Paper.io style territory capture. Use the same grid, player movement but now add an extra territory for each player.

## What you need

- Python 3
- `pygame` (`pip install pygame`)
- `numpy` (`pip install numpy`)


## 1. Understanding Trail & Territory

**Territory** — This is each player's captured area, make sure to differentiate it from trail.

**Trail** — The path left behind when you step off your territory. Touching your own trail kills you but touching an opponent's trail eliminates that opponent.

When you leave your territory and reconnect back to it, the area enclosed by your trail + territory border gets captured and added into the territory.


## 2. Grid Encoding

Each cell of grid has three states: empty, trail (and whose), territory (and whose). Pick a simple encoding that lets you check collisions in one line.

>**Example**:
    > grid[cell] = 0 -> empty, -N: player N's trail, +N : player N's territory


## 3. Trail System

- Players leave a trail only when they're **off** their territory.
- The trail is placed at the cell the player **vacates**, not their current position.
- After a successful capture, trail cells become territory and the trail disappears.


## 4. Territory Capture

When a player steps back onto their own territory after leaving a trail:

1. The trail + territory border forms a closed boundary
2. Everything inside that boundary gets captured
3. The trail cells also become territory

Use the flood fill algorithm you learnt last week from implementing the territory capture

## 5. Collision System

- Moving into your trail = death
- Moving into opponents trail = opponent's death
- Moving into opponent territory = blocked 
- Out of bounds = blocked
> But actually the real game allows to capture other's territory, play the paper.io game once

> **blocked** means that you will remain at that position unitl the direction is changed.

## 6. Rendering

Drawing 6400 rectangles one by one is slow. Build a color array from your grid and draw it all at once with `pygame.surfarray.blit_array()`. Draw player circles on top with `pygame.draw.circle()`.

Try to make the color array with simple numpy commands without any for loops, also dim the color of trail to differentiate with territory

## 7. File Structure

```
week3/
├── main.py
├── constants.py
├── player.py
├── game.py
├── renderer.py
├── capture.py
└── utils.py
```

## 8. Hints for each file

- **constants.py** — Colors, screen size, grid size, FPS. Same as Week 2
- **player.py** — Same Player class from Week 2. You might want to add a flag for whether the player is currently on or off their territory.
- **game.py** — Movement, trail placement, collision checks. You need to also trigger the capture here when a player reconnects to their territory.
- **capture.py** — The capture algorithm will be here. You can also ditch this file and implement it in game.py but this increases the modularity of code
- **renderer.py** — Build the color array from the grid and call blit_array.
- **main.py** — Game loop and keyboard input. Same structure as Week 2.
- **utils.py** - Optional file, if you implement any helper functions


## 9. BONUS (Optional)

- Capture opponent territory too
- Score display (territory count)
- Powerups, speed boosts ...


## Submission

Submit a zip file containing the entire WEEK-3 folder.
