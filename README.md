# SoC 2026 - RL Arena

This repository contains my work completed as part of the Summer of Code 2026 RL Arena.

## Week 1 - Python Basics

Implemented a simple grid-based game in Python with:
- Player movement using WASD keys
- Boundary checking
- Obstacles
- Modular project structure

## Week 2 - Pygame

Extended the Week 1 assignment using Pygame and NumPy.

Features:
- Two-player gameplay
- Trail generation
- Trail collision detection
- Head-on collision handling
- Real-time rendering

## Week 3 - Territory Capture Game

Implemented a Paper.io style territory capture game.

Features:
- Territory and trail systems
- Flood fill based territory capture
- Player elimination through trail collisions
- Territory stealing
- Score tracking
- Efficient rendering using NumPy and Pygame

This week was the most challenging because it involved handling many game logic edge cases and implementing the capture algorithm correctly.

## Week 4 - Reinforcement Learning

Learned the fundamentals of Reinforcement Learning and implemented a custom Gymnasium Maze environment trained using PPO.

A detailed summary of the concepts learned can be found in `WEEK-4/README.md`.

## Technologies Used

- Python
- NumPy
- Pygame
- Gymnasium
- Stable-Baselines3