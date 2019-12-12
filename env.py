# IN THIS FILE WE ONLY CREATE THE NECESSARY CLASS FOR MAKING THE ENVIRONMENT AND  CREATE THE Q-TABLE

################### IMPORTS #####################
import numpy as np
from PIL import Image, ImageDraw
import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
from collections import deque

style.use("ggplot")

################## CONSTANTS #####################
GAME_WIDTH=6
GAME_LENGTH=10
DODGE_GOAL=20 #Needs to dodge 20 bullets to reach final goal

TOT_EPISODES=15_000

MOVE_PENALTY=1
ENEMY_PENALTY=200
DODGE_REWARD=3
ALL_DODGE_REWARD=200

epsilon=0.5
EPS_DECAY=0.999
SHOW_EVERY=1000

LR=0.1 #LEARNING RATE
DISCOUNT=0.95

AGENT=1
BULLET=2
SHOOTER=3
d= {1: (255,0,0),
    2: (192, 192, 192),
    3: (0,0,255)
    }

############### ENVIRONMENT OBJECTS ###############
#Class for the agent
class agent:
    def __init__(self):
        self.pos = np.random.randint(0,GAME_WIDTH)

    def __str__(self):
        return f"{self.pos}"

    def action(self, choice):
        if choice==0:
            self.move(-1)
        elif choice==1:
            self.move(0)
        elif choice==2:
            self.move(1)

    def move(self, move_by):
        self.pos += move_by
        #To fix out of bounds movement
        if self.pos<0:
            self.pos=0
        elif self.pos>GAME_WIDTH-1:
            self.pos=GAME_WIDTH-1

#Class for the villain and the bullets
class villain_bullets:
    def __init__(self):
        self.vil_pos=np.random.randint(0,GAME_WIDTH)
        #list containing the positions of bullets seen in a game frame; -1 means not existing
        self.bullet_pos=deque([np.random.randint(-1,0) for i in range(GAME_LENGTH)])
        self.bullet_pos[GAME_LENGTH-1]=self.vil_pos
        self.observed_bullet=self.bullet_pos[1]
        self.final_bullet=self.bullet_pos[0]
        self.bullets_shot=0

    def move(self):
        if self.bullets_shot<DODGE_GOAL-1:
            self.vil_pos=np.random.randint(0,GAME_WIDTH)
            self.bullet_pos.popleft()
            self.bullet_pos.append(self.vil_pos)
            self.bullets_shot+=1
        else:
            self.vil_pos=GAME_WIDTH//2
            self.bullet_pos.popleft()
            self.bullet_pos.append(-1)

        self.observed_bullet=self.bullet_pos[1]
        self.final_bullet=self.bullet_pos[0]




############# MAKING THE Q-TABLE ##################
'''
Q TABLE==>(pos_agent,pos_bullet, tot_dodged) | act1 | act2 | act3
            (0,0,0)                          | 0.5  | 0    | 0.5
            .                                   .       .      .
            .                                   .       .      .
            .                                   .       .      .
'''
q_table={}
for i in range(0,GAME_WIDTH): #agent pos
    for j in range(-1, GAME_WIDTH): #bullet pos_bullet
        for k in range(0,DODGE_GOAL+1): #total bullets dodged
            q_table[(i,j,k)]=[np.random.uniform(-3,0) for i in range(3)]









































