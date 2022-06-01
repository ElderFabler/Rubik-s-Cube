#-----------------------------------------
#Author: me
#v.0.0.1
#have fun
#-----------------------------------------


import numpy as np
import random as rn
from collections import Counter

green = np.ones((3,3)).astype('<U1')
green[:] = 'g'
orange = np.ones((3,3)).astype('<U1')
orange[:] = 'o'
blue = np.ones((3,3)).astype('<U1')
blue[:] = 'b'
red = np.ones((3,3)).astype('<U1')
red[:] = 'r'
yellow = np.ones((3,3)).astype('<U1')
yellow[:] = 'y'
white = np.ones((3,3)).astype('<U1')
white[:] = 'w'

position = [
    {'front':green,'back':blue},
    {'left':orange,'right':red},
    {'top':white,'bot':yellow},
    ]
#pp = position[1]
def rotate_all(position):
    side = input('Enter side for rotate:\n')
    chg_ptn = {
        'left':[
            {'front':position[1]['right'],'back':position[1]['left']},
            {'left':position[0]['front'],'right':position[0]['back']},
            {'top':position[2]['top'],'bot':position[2]['bot']},
            ],
        'right':[
            {'front':position[1]['left'],'back':position[1]['right']},
            {'left':position[0]['back'],'right':position[0]['front']},
            {'top':position[2]['top'],'bot':position[2]['bot']},
            ],
        'up':[
            {'front':position[2]['bot'],'back':position[2]['top']},
            {'left':position[1]['left'],'right':position[1]['right']},
            {'top':position[0]['front'],'bot':position[0]['back']},
            ],
        'down':[
            {'front':position[2]['top'],'back':position[2]['bot']},
            {'left':position[1]['left'],'right':position[1]['right']},
            {'top':position[0]['back'],'bot':position[0]['front']},
            ],
        'reverse':[
            {'front':position[0]['back'],'back':position[0]['front']},
            {'left':position[1]['right'],'right':position[1]['left']},
            {'top':position[2]['top'],'bot':position[2]['bot']},
            ],
        'around':[
            {'front':position[0]['back'],'back':position[0]['front']},
            {'left':position[1]['left'],'right':position[1]['right']},
            {'top':position[2]['bot'],'bot':position[2]['top']},
            ],
        }
               
    position = chg_ptn[side]
    return position

position = rotate_all(position)
print(position)
print(position[0]['front'])

