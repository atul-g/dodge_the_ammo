# BULLET DODGER
A self-created reinforcement learning environment in which the agent learns to dodge bullets fired at it.

## Preview:
![alt](https://raw.githubusercontent.com/atul-g/dodge_the_ammo/master/episode_10000.gif)

## Environment:
The environment consists of 3 elements: the agent, the villain and bullets. The Villain shoots a series of bullets from any position, it is given the freedom to move at any random horizontal position at a fixed vertical distance from the Agent. The Agent tries to evade the bullets by moving either to it's left or right or by staying in it's curret position.

The created environment follows to be a simple Markov's Decision Process. Here the observation of the agent corresponds to it's own horizontal position, the position of the bullet at the row in front of it along with the number of bullets it has dodged in total.
This corresponds the state.

The action can have 3 values for the Agent as it can move either to it's right or to it's left. The 3rd option is to remain
at the same position. The environment makes sure that Agent and the Villain do not move out of the game's boundaries. The goal
of the Agent is to dodge a certain number of bullets in order to win the game. The environment was solved using a Q-table.

#### Rewards:
We penalize the Agent for moving in order to minimize it's movement as much as possible. The Agent is given a small reward for
each bullet it dodges. It receives a big penalty when it fails to do this or receives a large reward when it dodges all the
bullets fired at it by the Villain.

#### Q-Table:
The Q-table comprises of rows which correspond to the observation-space:   
**[agent position, bullet position, total dodged]**

The table consists of 3 columns each of which represents the 3 actions that Agent can take represented numerically.

#### Updating the Q-Table:
We basically follow this equation to compute the Q-value for the state that we are in:
![q-value formula](https://pythonprogramming.net/static/images/reinforcement-learning/new-q-value-formula.png)  

## Learning:
Here are few gifs showing how the Agent was able to perform at certain episodes:  

![ep_2](https://github.com/atul-g/dodge_the_ammo/blob/master/episode_2.gif) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![ep_217](https://github.com/atul-g/dodge_the_ammo/blob/master/episode_217.gif)  

![ep_3500](https://github.com/atul-g/dodge_the_ammo/blob/master/episode_3500.gif) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![ep_10000](https://github.com/atul-g/dodge_the_ammo/blob/master/episode_10000.gif)


The Agent was trained for around 15,000 episodes and here is the graph showing the rolling-average of rewards it earned at every 1000 episodes.  
![graph](https://github.com/atul-g/dodge_the_ammo/blob/master/avg_reward.png)

## Running the files:
You can run the episodes.py file to start the learning of the Agent. The env.py file consists of the Agent, Villain classes and the Q-table was also initialized here.

## Resources:
https://youtu.be/G92TF4xYQcU
