# BULLET DODGER
A self-created reinforcement learning environment in which the agent tries to learn to dodge bullets fired at it.

## Preview:
![alt](https://raw.githubusercontent.com/atul-g/dodge_the_ammo/master/episode_10000.gif)

## Environment:
The environment consists of 3 elements: the agent, the villain and bullets. The Villain shoots a series of bullets from any position, it is given the freedom to move at any random horizontal position at a fixed vertical distance from the Agent. The Agent tries to evade the bullets by moving either to it's left or right or by staying in it's curret position.

The created environment follows to be a simple Markov's Decision Process. Here the observation of the agent corresponds to it's own horizontal position, the position of the bullet at the row in front of it along with the number of bullets it has dodged in total.
This corresponds the state.

The action can have 3 values for the Agent as it can move either to it's right or to it's left. The 3rd option is to remain
at the same position. The environment makes sure that Agent and the Villain do not move out of the game's boundaries. The goal
of the Agent is to dodge a certain number of bullets in order to win the game. The environment was solved using a Q-table.

### Rewards:
We penalize the Agent for moving in order to minimize it's movement as much as possible. The Agent is given a small reward for
each bullet it dodges. It receives a big penalty when it fails to do this or receives a large reward when it dodges all the
bullets fired at it by the Villain.

### Q-Table:
The Q-table comprises of rows which correspond to the observation-space:   
**[agent position, bullet position, total dodged]**

The table consists of 3 columns each of which represents the 3 actions that Agent can take represented numerically.

###
