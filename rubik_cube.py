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

#pp = position[1]
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

        position = [
            {'front':green,'back':blue},
            {'left':orange,'right':red},
            {'top':white,'bot':yellow},
        ]
        self.position = position

    def rotate_all(self,side):
        chg_ptn = {
            'left':[
                {'front':self.position[1]['right'],'back':self.position[1]['left']},
                {'left':self.position[0]['front'],'right':self.position[0]['back']},
                {'top':np.rot90(self.position[2]['top'],3),'bot':np.rot90(self.position[2]['bot'])},
                ],
            'right':[
                {'front':self.position[1]['left'],'back':self.position[1]['right']},
                {'left':self.position[0]['back'],'right':self.position[0]['front']},
                {'top':np.rot90(self.position[2]['top']),'bot':np.rot90(self.position[2]['bot'],3)},
                ],
            'up':[
                {'front':self.position[2]['bot'],'back':np.rot90(np.rot90(self.position[2]['top']))},
                {'left':np.rot90(self.position[1]['left']),'right':np.rot90(self.position[1]['right'],3)},
                {'top':self.position[0]['front'],'bot':np.rot90(np.rot90(self.position[0]['back']))},
                ],
            'down':[
                {'front':self.position[2]['top'],'back':np.rot90(np.rot90(self.position[2]['bot']))},
                {'left':np.rot90(self.position[1]['left'],3),'right':np.rot90(self.position[1]['right'])},
                {'top':np.rot90(np.rot90(self.position[0]['back'])),'bot':self.position[0]['front']},
                ],
            'reverse':[
                {'front':self.position[0]['back'],'back':self.position[0]['front']},
                {'left':self.position[1]['right'],'right':self.position[1]['left']},
                {'top':np.rot90(np.rot90(self.position[2]['top'])),'bot':np.rot90(np.rot90(self.position[2]['bot']))},
                ],
            'around':[
                {'front':np.rot90(np.rot90(self.position[0]['back'])),'back':np.rot90(np.rot90(self.position[0]['front']))},
                {'left':np.rot90(np.rot90(self.position[1]['left'])),'right':np.rot90(np.rot90(self.position[1]['right']))},
                {'top':self.position[2]['bot'],'bot':self.position[2]['top']},
                ],
            }               
        self.position = chg_ptn[side]
        return self.position

    def rotate_edge(self,row_col,side):
        chg_ptn = {
            "top":{
                "left":[
                    {
                        "front":np.array([
                            self.position[1]['right'][0,:],
                            self.position[0]['front'][1,:],
                            self.position[0]['front'][2,:],
                        ]),
                        "back":np.array([
                            self.position[1]['left'][0,:],
                            self.position[0]['back'][1,:],
                            self.position[0]['back'][2,:],
                        ])
                    },
                    {
                        "left":np.array([
                            self.position[0]['front'][0,:],
                            self.position[1]['left'][1,:],
                            self.position[1]['left'][2,:],
                        ]),
                        "right":np.array([
                            self.position[0]['back'][0,:],
                            self.position[1]['right'][1,:],
                            self.position[1]['right'][2,:],
                        ])
                    },
                    {
                        "top":np.array([
                            self.position[2]['top'][2],
                            self.position[2]['top'][1],
                            self.position[2]['top'][0],
                        ]).transpose(),
                        "bot":self.position[2]['bot']
                    }
                ],
                "right":[
                    {
                        "front":np.array([
                            self.position[1]['left'][0,:],
                            self.position[0]['front'][1,:],
                            self.position[0]['front'][2,:],
                        ]),
                        "back":np.array([
                            self.position[1]['right'][0,:],
                            self.position[0]['back'][1,:],
                            self.position[0]['back'][2,:],
                        ])
                    },
                    {
                        "left":np.array([
                            self.position[0]['back'][0,:],
                            self.position[1]['left'][1,:],
                            self.position[1]['left'][2,:],
                        ]),
                        "right":np.array([
                            self.position[0]['front'][0,:],
                            self.position[1]['right'][1,:],
                            self.position[1]['right'][2,:],
                        ])
                    },
                    {
                        "top":np.array([
                            self.position[2]['top'][0,::-1],
                            self.position[2]['top'][1,::-1],
                            self.position[2]['top'][2,::-1],
                        ]).transpose(),
                        "bot":self.position[2]['bot']
                    }
                ]
            },
            "mid":{
                "left":[
                    {
                        "front":np.array([
                            self.position[0]['front'][0,:],
                            self.position[1]['right'][1,:],
                            self.position[0]['front'][2,:],
                        ]),
                        "back":np.array([
                            self.position[0]['back'][0,:],
                            self.position[1]['left'][1,:],
                            self.position[0]['back'][2,:],
                        ])
                    },
                    {
                        "left":np.array([
                            self.position[1]['left'][0,:],
                            self.position[0]['front'][1,:],
                            self.position[1]['left'][2,:],
                        ]),
                        "right":np.array([
                            self.position[1]['right'][0,:],
                            self.position[0]['back'][1,:],
                            self.position[1]['right'][2,:],
                        ])
                    },
                    {
                        "top":self.position[2]['top'],
                        "bot":self.position[2]['bot']
                    }
                ],
                "right":[
                    {
                        "front":np.array([
                            self.position[0]['front'][0,:],
                            self.position[1]['left'][1,:],
                            self.position[0]['front'][2,:],
                        ]),
                        "back":np.array([
                            self.position[0]['back'][0,:],
                            self.position[1]['right'][1,:],
                            self.position[0]['back'][2,:],
                        ])
                    },
                    {
                        "left":np.array([
                            self.position[1]['left'][0,:],
                            self.position[0]['back'][1,:],
                            self.position[1]['left'][2,:],
                        ]),
                        "right":np.array([
                            self.position[1]['right'][0,:],
                            self.position[0]['front'][1,:],
                            self.position[1]['right'][2,:],
                        ])
                    },
                    {
                        "top":self.position[2]['top'],
                        "bot":self.position[2]['bot']
                    }
                ]
            },
            "bot":{
                "left":[
                    {
                        "front":np.array([
                            self.position[0]['front'][0,:],
                            self.position[0]['front'][1,:],
                            self.position[1]['right'][2,:],
                        ]),
                        "back":np.array([
                            self.position[0]['back'][0,:],
                            self.position[0]['back'][1,:],
                            self.position[1]['left'][2,:],
                        ])
                    },
                    {
                        "left":np.array([
                            self.position[1]['left'][0,:],
                            self.position[1]['left'][1,:],
                            self.position[0]['front'][2,:],
                        ]),
                        "right":np.array([
                            self.position[1]['right'][0,:],
                            self.position[1]['right'][1,:],
                            self.position[0]['back'][2,:],
                        ])
                    },
                    {
                        "top":self.position[2]['top'],
                        "bot":np.array([
                            self.position[2]['bot'][:,2],
                            self.position[2]['bot'][:,1],
                            self.position[2]['bot'][:,0],
                        ]),
                    }
                ],
                "right":[
                    {
                        "front":np.array([
                            self.position[0]['front'][0,:],
                            self.position[0]['front'][1,:],
                            self.position[1]['left'][2,:],
                        ]),
                        "back":np.array([
                            self.position[0]['back'][0,:],
                            self.position[0]['back'][1,:],
                            self.position[1]['right'][2,:],
                        ])
                    },
                    {
                        "left":np.array([
                            self.position[1]['left'][0,:],
                            self.position[1]['left'][1,:],
                            self.position[0]['back'][2,:],
                        ]),
                        "right":np.array([
                            self.position[1]['right'][0,:],
                            self.position[1]['right'][1,:],
                            self.position[0]['front'][2,:],
                        ])
                    },
                    {
                        "top":self.position[2]['top'],
                        "bot":np.array([
                            self.position[2]['bot'][::-1,0],
                            self.position[2]['bot'][::-1,1],
                            self.position[2]['bot'][::-1,2],
                        ]),
                    }
                ]
            },
            "left":{
                "up":[
                    {
                        "front":np.array([
                            self.position[2]['bot'][:,0],
                            self.position[0]['front'][:,1],
                            self.position[0]['front'][:,2],
                        ]).transpose(),
                        "back":np.array([
                            self.position[0]['back'][:,0],
                            self.position[0]['back'][:,1],
                            self.position[2]['top'][::-1,0],
                        ]).transpose()
                    },
                    {
                        "left":np.array([
                            self.position[1]['left'][0,::-1],
                            self.position[1]['left'][1,::-1],
                            self.position[1]['left'][2,::-1],
                        ]).transpose(),
                        "right":self.position[1]['right']
                    },
                    {
                        "top":np.array([
                            self.position[0]['front'][:,0],
                            self.position[2]['top'][:,1],
                            self.position[2]['top'][:,2],
                        ]).transpose(),
                        "bot":np.array([
                            self.position[0]['back'][::-1,2],
                            self.position[2]['bot'][:,1],
                            self.position[2]['bot'][:,2],
                        ]).transpose()
                    },
                ],
                "down":[
                    {
                        "front":np.array([
                            self.position[2]['top'][:,0],
                            self.position[0]['front'][:,1],
                            self.position[0]['front'][:,2],
                        ]).transpose(),
                        "back":np.array([
                            self.position[0]['back'][:,0],
                            self.position[0]['back'][:,1],
                            self.position[2]['bot'][::-1,0],
                        ]).transpose()
                    },
                    {
                        "left":np.array([
                            self.position[1]['left'][2],
                            self.position[1]['left'][1],
                            self.position[1]['left'][0],
                        ]).transpose(),
                        "right":self.position[1]['right']
                    },
                    {
                        "top":np.array([
                            self.position[0]['back'][::-1,2],
                            self.position[2]['top'][:,1],
                            self.position[2]['top'][:,2],
                        ]).transpose(),
                        "bot":np.array([
                            self.position[0]['front'][:,0],
                            self.position[2]['bot'][:,1],
                            self.position[2]['bot'][:,2],
                        ]).transpose()
                    },
                ],
            },
            "center":{
                "up":[
                    {
                        "front":np.array([
                            self.position[0]['front'][:,0],
                            self.position[2]['bot'][:,1],
                            self.position[0]['front'][:,2],
                        ]).transpose(),
                        "back":np.array([
                            self.position[0]['back'][:,0],
                            self.position[2]['top'][::-1,1],
                            self.position[0]['back'][:,2],
                        ]).transpose()
                    },
                    {
                        "left":self.position[1]['left'],
                        "right":self.position[1]['right']
                    },
                    {
                        "top":np.array([
                            self.position[2]['top'][:,0],
                            self.position[0]['front'][:,1],
                            self.position[2]['top'][:,2],
                        ]).transpose(),
                        "bot":np.array([
                            self.position[2]['bot'][:,0],
                            self.position[0]['back'][::-1,1],
                            self.position[2]['bot'][:,2],
                        ]).transpose()
                    },
                ],
                "down":[
                    {
                        "front":np.array([
                            self.position[0]['front'][:,0],
                            self.position[2]['top'][:,1],
                            self.position[0]['front'][:,2],
                        ]).transpose(),
                        "back":np.array([
                            self.position[0]['back'][:,0],
                            self.position[2]['bot'][:,1],
                            self.position[0]['back'][:,2],
                        ]).transpose()
                    },
                    {
                        "left":self.position[1]['left'],
                        "right":self.position[1]['right']
                    },
                    {
                        "top":np.array([
                            self.position[2]['top'][:,0],
                            self.position[0]['back'][::-1,1],
                            self.position[2]['top'][:,2],
                        ]).transpose(),
                        "bot":np.array([
                            self.position[2]['bot'][:,0],
                            self.position[0]['front'][:,1],
                            self.position[2]['bot'][:,2],
                        ]).transpose()
                    },
                ],
            },
            "right":{
                "up":[
                    {
                        "front":np.array([
                            self.position[0]['front'][:,0],
                            self.position[0]['front'][:,1],
                            self.position[2]['bot'][:,2],
                        ]).transpose(),
                        "back":np.array([
                            self.position[2]['top'][::-1,2],
                            self.position[0]['back'][:,1],
                            self.position[0]['back'][:,2],
                        ]).transpose()
                    },
                    {
                        "left":self.position[1]['left'],
                        "right":np.array([
                            self.position[1]['right'][::-1,0],
                            self.position[1]['right'][::-1,1],
                            self.position[1]['right'][::-1,2],
                        ]),
                    },
                    {
                        "top":np.array([
                            self.position[2]['top'][:,0],
                            self.position[2]['top'][:,1],
                            self.position[0]['front'][:,2],
                        ]).transpose(),
                        "bot":np.array([
                            self.position[2]['bot'][:,0],
                            self.position[2]['bot'][:,1],
                            self.position[0]['back'][::-1,0],
                        ]).transpose()
                    },
                ],
                "down":[
                    {
                        "front":np.array([
                            self.position[0]['front'][:,0],
                            self.position[0]['front'][:,1],
                            self.position[2]['top'][:,2],
                        ]).transpose(),
                        "back":np.array([
                            self.position[2]['bot'][::-1,2],
                            self.position[0]['back'][:,1],
                            self.position[0]['back'][:,2],
                        ]).transpose()
                    },
                    {
                        "left":self.position[1]['left'],
                        "right":np.array([
                            self.position[1]['right'][0,::-1],
                            self.position[1]['right'][1,::-1],
                            self.position[1]['right'][2,::-1],
                        ]).transpose(),
                    },
                    {
                        "top":np.array([
                            self.position[2]['top'][:,0],
                            self.position[2]['top'][:,1],
                            self.position[0]['back'][::-1,0],
                        ]).transpose(),
                        "bot":np.array([
                            self.position[2]['bot'][:,0],
                            self.position[2]['bot'][:,1],
                            self.position[0]['front'][:,2],
                        ]).transpose()
                    },
                ],
            },
        }
        self.position = chg_ptn[row_col][side]
        return self.position

    def rand_pos(self,ran = 10):
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
        for i in range(0,20):
            row_col = choice(list(rotedgedi.keys()))
            funcdi = [
                "self.rotate_all(choice(rotallli))",
                "self.rotate_edge(row_col,choice(list(rotedgedi[row_col])))",
            ]
            randrot = eval(choice(funcdi))
            pos.append(randrot)
        self.position = pos[-1]
        return self.position, pos



""" while True:
    self.position = rotate_edge(self.position)
    print(self.position[0]['front'])
    print(self.position[0]['back'])
    print(self.position[1]['left'])
    print(self.position[1]['right'])
    print(self.position[2]['top'])
    print(self.position[2]['bot'])

 """