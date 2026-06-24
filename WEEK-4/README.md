# Week 4 - Reinforcement Learning

This week was focused on learning the basics of Reinforcement Learning (RL) and understanding how agents learn by interacting with an environment.

## What I Learned

### Reinforcement Learning Basics

In Reinforcement Learning, an agent learns by taking actions in an environment and receiving rewards based on those actions.

The main components are:

- Agent
- Environment
- Observation (State)
- Action
- Reward

The goal of the agent is to maximize the total reward it receives.

### Gymnasium Environments

I learned how RL environments are implemented using Gymnasium.

Important methods in a custom environment:

- `__init__()` – initialize the environment
- `reset()` – start a new episode
- `step(action)` – execute an action and return the result
- `_get_obs()` – generate observations for the agent
- `_render_rgb()` – visualize the environment

### Observation Space

The observation space defines what information the agent can see.

In the maze environment:
- Walls
- Empty cells
- Goal position
- Agent position

were encoded into a NumPy array and provided to the agent as observations.

I also learned why observations are often normalized and stored as `float32` values.

### Action Space

The action space defines the actions available to the agent.

For the maze environment:

- Up
- Right
- Down
- Left

were represented using a discrete action space.

### Rewards

I learned that reward design is one of the most important parts of Reinforcement Learning.

For the maze environment:

- Reaching the goal gives a positive reward
- Hitting a wall gives a penalty
- Revisiting cells gives a penalty
- Normal movement gives a small penalty

These rewards encourage the agent to find efficient paths to the goal.

### Terminated vs Truncated

I learned the difference between:

- `terminated` – the episode ended because the objective was reached
- `truncated` – the episode ended because a limit such as maximum steps was reached

### PPO (Proximal Policy Optimization)

I learned about PPO, a popular Reinforcement Learning algorithm available in Stable-Baselines3.

PPO improves the agent's policy using experience collected from interactions with the environment while maintaining stable learning.

## Practical Implementation

As part of this week, I implemented a custom Maze environment using Gymnasium.

The environment included:

- A custom observation space
- A discrete action space
- Reward design
- Episode reset and termination logic
- RGB rendering for visualization

I then trained an agent using PPO and successfully tested it on the maze.

## Key Takeaways

- Reinforcement Learning is based on learning through rewards rather than labeled data.
- Reward design has a significant impact on agent behavior.
- Observation and action spaces are fundamental to environment design.
- Gymnasium provides a standard framework for creating RL environments.
- PPO can successfully learn policies for custom environments.