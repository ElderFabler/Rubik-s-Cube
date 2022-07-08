#-----------------------------------------
#Author: me
#v.0.0.2 - Added rotate-edges func
#v.0.0.3 - Fixing rotate-edges func
#have fun
#-----------------------------------------


import numpy as np
import random as rn
from collections import Counter
from random import choice

#pp = position[0]
class Rubik_cube(object):
    def __init__(self):
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

        self.pos = []

        self.position = [{
            'front':green,'back':blue,
            'left':orange,'right':red,
            'top':white,'bot':yellow
        }]

    def rotate_all(self,side):
        chg_ptn = {
            'left':[{
                'front':self.position[0]['right'],'back':self.position[0]['left'],
                'left':self.position[0]['front'],'right':self.position[0]['back'],
                'top':np.rot90(self.position[0]['top'],3),'bot':np.rot90(self.position[0]['bot']),
            }],
            'right':[{
                'front':self.position[0]['left'],'back':self.position[0]['right'],
                'left':self.position[0]['back'],'right':self.position[0]['front'],
                'top':np.rot90(self.position[0]['top']),'bot':np.rot90(self.position[0]['bot'],3),
            }],
            'up':[{
                'front':self.position[0]['bot'],'back':np.rot90(np.rot90(self.position[0]['top'])),
                'left':np.rot90(self.position[0]['left']),'right':np.rot90(self.position[0]['right'],3),
                'top':self.position[0]['front'],'bot':np.rot90(np.rot90(self.position[0]['back'])),
            }],
            'down':[{
                'front':self.position[0]['top'],'back':np.rot90(np.rot90(self.position[0]['bot'])),
                'left':np.rot90(self.position[0]['left'],3),'right':np.rot90(self.position[0]['right']),
                'top':np.rot90(np.rot90(self.position[0]['back'])),'bot':self.position[0]['front'],
            }],
            'reverse':[{
                'front':self.position[0]['back'],'back':self.position[0]['front'],
                'left':self.position[0]['right'],'right':self.position[0]['left'],
                'top':np.rot90(np.rot90(self.position[0]['top'])),'bot':np.rot90(np.rot90(self.position[0]['bot'])),
            }],
            'around':[{
                'front':np.rot90(np.rot90(self.position[0]['back'])),'back':np.rot90(np.rot90(self.position[0]['front'])),
                'left':np.rot90(np.rot90(self.position[0]['left'])),'right':np.rot90(np.rot90(self.position[0]['right'])),
                'top':self.position[0]['bot'],'bot':self.position[0]['top']
            }],
            }               
        self.position = chg_ptn[side]
        return self.position

    def rotate_edge(self,row_col,side):
        chg_ptn = {
            "top":{
                "left":[{                    
                    "front":np.array([
                        self.position[0]['right'][0,:],
                        self.position[0]['front'][1,:],
                        self.position[0]['front'][2,:],
                    ]),
                    "back":np.array([
                        self.position[0]['left'][0,:],
                        self.position[0]['back'][1,:],
                        self.position[0]['back'][2,:],
                    ]),
                    "left":np.array([
                        self.position[0]['front'][0,:],
                        self.position[0]['left'][1,:],
                        self.position[0]['left'][2,:],
                    ]),
                    "right":np.array([
                        self.position[0]['back'][0,:],
                        self.position[0]['right'][1,:],
                        self.position[0]['right'][2,:],
                    ]),
                    "top":np.array([
                        self.position[0]['top'][2],
                        self.position[0]['top'][1],
                        self.position[0]['top'][0],
                    ]).transpose(),
                    "bot":self.position[0]['bot']
                }],
                "right":[{
                    "front":np.array([
                        self.position[0]['left'][0,:],
                        self.position[0]['front'][1,:],
                        self.position[0]['front'][2,:],
                    ]),
                    "back":np.array([
                        self.position[0]['right'][0,:],
                        self.position[0]['back'][1,:],
                        self.position[0]['back'][2,:],
                    ]),
                    "left":np.array([
                        self.position[0]['back'][0,:],
                        self.position[0]['left'][1,:],
                        self.position[0]['left'][2,:],
                    ]),
                    "right":np.array([
                        self.position[0]['front'][0,:],
                        self.position[0]['right'][1,:],
                        self.position[0]['right'][2,:],
                    ]),
                    "top":np.array([
                        self.position[0]['top'][0,::-1],
                        self.position[0]['top'][1,::-1],
                        self.position[0]['top'][2,::-1],
                    ]).transpose(),
                    "bot":self.position[0]['bot']
                }],
            },
            "mid":{
                "left":[{
                    "front":np.array([
                        self.position[0]['front'][0,:],
                        self.position[0]['right'][1,:],
                        self.position[0]['front'][2,:],
                    ]),
                    "back":np.array([
                        self.position[0]['back'][0,:],
                        self.position[0]['left'][1,:],
                        self.position[0]['back'][2,:],
                    ]),
                    "left":np.array([
                        self.position[0]['left'][0,:],
                        self.position[0]['front'][1,:],
                        self.position[0]['left'][2,:],
                    ]),
                    "right":np.array([
                        self.position[0]['right'][0,:],
                        self.position[0]['back'][1,:],
                        self.position[0]['right'][2,:],
                    ]),
                    "top":self.position[0]['top'],
                    "bot":self.position[0]['bot']
                }],
                "right":[{
                    "front":np.array([
                        self.position[0]['front'][0,:],
                        self.position[0]['left'][1,:],
                        self.position[0]['front'][2,:],
                    ]),
                    "back":np.array([
                        self.position[0]['back'][0,:],
                        self.position[0]['right'][1,:],
                        self.position[0]['back'][2,:],
                    ]),
                    "left":np.array([
                        self.position[0]['left'][0,:],
                        self.position[0]['back'][1,:],
                        self.position[0]['left'][2,:],
                    ]),
                    "right":np.array([
                        self.position[0]['right'][0,:],
                        self.position[0]['front'][1,:],
                        self.position[0]['right'][2,:],
                    ]),
                    "top":self.position[0]['top'],
                    "bot":self.position[0]['bot']
                }],
            },
            "bot":{
                "left":[{
                    "front":np.array([
                        self.position[0]['front'][0,:],
                        self.position[0]['front'][1,:],
                        self.position[0]['right'][2,:],
                    ]),
                    "back":np.array([
                        self.position[0]['back'][0,:],
                        self.position[0]['back'][1,:],
                        self.position[0]['left'][2,:],
                    ]),
                    "left":np.array([
                        self.position[0]['left'][0,:],
                        self.position[0]['left'][1,:],
                        self.position[0]['front'][2,:],
                    ]),
                    "right":np.array([
                        self.position[0]['right'][0,:],
                        self.position[0]['right'][1,:],
                        self.position[0]['back'][2,:],
                    ]),
                    "top":self.position[0]['top'],
                    "bot":np.array([
                        self.position[0]['bot'][:,2],
                        self.position[0]['bot'][:,1],
                        self.position[0]['bot'][:,0],
                    ]),
                }],
                "right":[{
                    "front":np.array([
                        self.position[0]['front'][0,:],
                        self.position[0]['front'][1,:],
                        self.position[0]['left'][2,:],
                    ]),
                    "back":np.array([
                        self.position[0]['back'][0,:],
                        self.position[0]['back'][1,:],
                        self.position[0]['right'][2,:],
                    ]),
                    "left":np.array([
                        self.position[0]['left'][0,:],
                        self.position[0]['left'][1,:],
                        self.position[0]['back'][2,:],
                    ]),
                    "right":np.array([
                        self.position[0]['right'][0,:],
                        self.position[0]['right'][1,:],
                        self.position[0]['front'][2,:],
                    ]),
                    "top":self.position[0]['top'],
                    "bot":np.array([
                        self.position[0]['bot'][::-1,0],
                        self.position[0]['bot'][::-1,1],
                        self.position[0]['bot'][::-1,2],
                    ]),
                }],
            },
            "left":{
                "up":[{
                    "front":np.array([
                        self.position[0]['bot'][:,0],
                        self.position[0]['front'][:,1],
                        self.position[0]['front'][:,2],
                    ]).transpose(),
                    "back":np.array([
                        self.position[0]['back'][:,0],
                        self.position[0]['back'][:,1],
                        self.position[0]['top'][::-1,0],
                    ]).transpose(),
                    "left":np.array([
                        self.position[0]['left'][0,::-1],
                        self.position[0]['left'][1,::-1],
                        self.position[0]['left'][2,::-1],
                    ]).transpose(),
                    "right":self.position[0]['right'],
                    "top":np.array([
                        self.position[0]['front'][:,0],
                        self.position[0]['top'][:,1],
                        self.position[0]['top'][:,2],
                    ]).transpose(),
                    "bot":np.array([
                        self.position[0]['back'][::-1,2],
                        self.position[0]['bot'][:,1],
                        self.position[0]['bot'][:,2],
                    ]).transpose()
                }],
                "down":[{
                    "front":np.array([
                        self.position[0]['top'][:,0],
                        self.position[0]['front'][:,1],
                        self.position[0]['front'][:,2],
                    ]).transpose(),
                    "back":np.array([
                        self.position[0]['back'][:,0],
                        self.position[0]['back'][:,1],
                        self.position[0]['bot'][::-1,0],
                    ]).transpose(),
                    "left":np.array([
                        self.position[0]['left'][2],
                        self.position[0]['left'][1],
                        self.position[0]['left'][0],
                    ]).transpose(),
                    "right":self.position[0]['right'],
                    "top":np.array([
                        self.position[0]['back'][::-1,2],
                        self.position[0]['top'][:,1],
                        self.position[0]['top'][:,2],
                    ]).transpose(),
                    "bot":np.array([
                        self.position[0]['front'][:,0],
                        self.position[0]['bot'][:,1],
                        self.position[0]['bot'][:,2],
                    ]).transpose(),
                }],
            },
            "center":{
                "up":[{
                    "front":np.array([
                        self.position[0]['front'][:,0],
                        self.position[0]['bot'][:,1],
                        self.position[0]['front'][:,2],
                    ]).transpose(),
                    "back":np.array([
                        self.position[0]['back'][:,0],
                        self.position[0]['top'][::-1,1],
                        self.position[0]['back'][:,2],
                    ]).transpose(),
                    "left":self.position[0]['left'],
                    "right":self.position[0]['right'],
                    "top":np.array([
                        self.position[0]['top'][:,0],
                        self.position[0]['front'][:,1],
                        self.position[0]['top'][:,2],
                    ]).transpose(),
                    "bot":np.array([
                        self.position[0]['bot'][:,0],
                        self.position[0]['back'][::-1,1],
                        self.position[0]['bot'][:,2],
                    ]).transpose()
                }],
                "down":[{
                    "front":np.array([
                        self.position[0]['front'][:,0],
                        self.position[0]['top'][:,1],
                        self.position[0]['front'][:,2],
                    ]).transpose(),
                    "back":np.array([
                        self.position[0]['back'][:,0],
                        self.position[0]['bot'][::-1,1],
                        self.position[0]['back'][:,2],
                    ]).transpose(),
                    "left":self.position[0]['left'],
                    "right":self.position[0]['right'],
                    "top":np.array([
                        self.position[0]['top'][:,0],
                        self.position[0]['back'][::-1,1],
                        self.position[0]['top'][:,2],
                    ]).transpose(),
                    "bot":np.array([
                        self.position[0]['bot'][:,0],
                        self.position[0]['front'][:,1],
                        self.position[0]['bot'][:,2],
                    ]).transpose()
                }],
            },
            "right":{
                "up":[{
                    "front":np.array([
                        self.position[0]['front'][:,0],
                        self.position[0]['front'][:,1],
                        self.position[0]['bot'][:,2],
                    ]).transpose(),
                    "back":np.array([
                        self.position[0]['top'][::-1,2],
                        self.position[0]['back'][:,1],
                        self.position[0]['back'][:,2],
                    ]).transpose(),
                    "left":self.position[0]['left'],
                    "right":np.array([
                        self.position[0]['right'][::-1,0],
                        self.position[0]['right'][::-1,1],
                        self.position[0]['right'][::-1,2],
                    ]),
                    "top":np.array([
                        self.position[0]['top'][:,0],
                        self.position[0]['top'][:,1],
                        self.position[0]['front'][:,2],
                    ]).transpose(),
                    "bot":np.array([
                        self.position[0]['bot'][:,0],
                        self.position[0]['bot'][:,1],
                        self.position[0]['back'][::-1,0],
                    ]).transpose()
                }],
                "down":[{
                    "front":np.array([
                        self.position[0]['front'][:,0],
                        self.position[0]['front'][:,1],
                        self.position[0]['top'][:,2],
                    ]).transpose(),
                    "back":np.array([
                        self.position[0]['bot'][::-1,2],
                        self.position[0]['back'][:,1],
                        self.position[0]['back'][:,2],
                    ]).transpose(),
                    "left":self.position[0]['left'],
                    "right":np.array([
                        self.position[0]['right'][0,::-1],
                        self.position[0]['right'][1,::-1],
                        self.position[0]['right'][2,::-1],
                    ]).transpose(),
                    "top":np.array([
                        self.position[0]['top'][:,0],
                        self.position[0]['top'][:,1],
                        self.position[0]['back'][::-1,0],
                    ]).transpose(),
                    "bot":np.array([
                        self.position[0]['bot'][:,0],
                        self.position[0]['bot'][:,1],
                        self.position[0]['front'][:,2],
                    ]).transpose()
                }],
            },
        }
        self.position = chg_ptn[row_col][side]
        return self.position

    def rand_pos(self,ran = 400):
        wfunc = ['all','edge']
        rotallli = ['left','right','up','down','reverse','around']
        rotedgedi = {
            'left':['up','down'],
            'center':['up','down'],
            'right':['up','down'],
            'top':['left','right'],
            'mid':['left','right'],
            'bot':['left','right'],
        }
        pos = []
        for i in range(0,ran):
            side = choice(list(rotallli))
            row_col = choice(list(rotedgedi.keys()))
            funcdi = [
                "self.rotate_all(choice(list(rotallli)))",
                "self.rotate_edge(row_col,choice(list(rotedgedi[row_col])))",
            ]
            randrot = eval(choice(funcdi))
            self.pos.append(randrot)
        self.position = self.pos[-1]
        return self.position, pos



if __name__ == "__main__":
    a = Rubik_cube()
    a.rand_pos()
    print(a.position)