import unittest
from rubik_cube import Rubik_cube

top_left = [
    {'front':[
        ['r', 'r', 'r'],
        ['g', 'g', 'g'],
        ['g', 'g', 'g']
        ],
    'back':[
        ['o', 'o', 'o'],
        ['b', 'b', 'b'],
        ['b', 'b', 'b']
        ]},
    {'left':[
        ['g', 'g', 'g'],
        ['o', 'o', 'o'],
        ['o', 'o', 'o']
        ], 
    'right':[
        ['b', 'b', 'b'],
        ['r', 'r', 'r'],
        ['r', 'r', 'r']
        ]}, 
    {'top':[
        ['w', 'w', 'w'],
        ['w', 'w', 'w'],
        ['w', 'w', 'w']
        ], 
    'bot':[
        ['y', 'y', 'y'],
        ['y', 'y', 'y'],
        ['y', 'y', 'y']
        ]}
        ]
right_down = [
    {'front':[
        ['r', 'r', 'w'],
        ['g', 'g', 'w'],
        ['g', 'g', 'w']
        ],
    'back':[
        ['y', 'o', 'o'],
        ['y', 'b', 'b'],
        ['y', 'b', 'b']
        ]},
    {'left':[
        ['g', 'g', 'g'],
        ['o', 'o', 'o'],
        ['o', 'o', 'o']
        ], 
    'right':[
        ['b', 'r', 'r'],
        ['b', 'r', 'r'],
        ['b', 'r', 'r']
        ]}, 
    {'top':[
        ['w', 'w', 'b'],
        ['w', 'w', 'b'],
        ['w', 'w', 'o']
        ], 
    'bot':[
        ['y', 'y', 'r'],
        ['y', 'y', 'g'],
        ['y', 'y', 'g']
        ]}
        ]
left_up = [
    {'front':[
        ['y', 'r', 'w'],
        ['y', 'g', 'w'],
        ['y', 'g', 'w']
        ],
    'back':[
        ['y', 'o', 'w'],
        ['y', 'b', 'w'],
        ['y', 'b', 'w']
        ]},
    {'left':[
        ['g', 'o', 'o'],
        ['g', 'o', 'o'],
        ['g', 'o', 'o']
        ], 
    'right':[
        ['b', 'r', 'r'],
        ['b', 'r', 'r'],
        ['b', 'r', 'r']
        ]}, 
    {'top':[
        ['r', 'w', 'b'],
        ['g', 'w', 'b'],
        ['g', 'w', 'o']
        ], 
    'bot':[
        ['b', 'y', 'r'],
        ['b', 'y', 'g'],
        ['o', 'y', 'g']
        ]}
        ]
bot_right = [
    {'front':[
        ['y', 'r', 'w'],
        ['y', 'g', 'w'],
        ['g', 'o', 'o']
        ],
    'back':[
        ['y', 'o', 'w'],
        ['y', 'b', 'w'],
        ['b', 'r', 'r']
        ]},
    {'left':[
        ['g', 'o', 'o'],
        ['g', 'o', 'o'],
        ['y', 'b', 'w']
        ], 
    'right':[
        ['b', 'r', 'r'],
        ['b', 'r', 'r'],
        ['y', 'g', 'w']
        ]}, 
    {'top':[
        ['r', 'w', 'b'],
        ['g', 'w', 'b'],
        ['g', 'w', 'o']
        ], 
    'bot':[
        ['o', 'b', 'b'],
        ['y', 'y', 'y'],
        ['g', 'g', 'r']
        ]}
        ]

top_right = [
    {'front':[
        ['g', 'o', 'o'],
        ['y', 'g', 'w'],
        ['g', 'o', 'o']
        ],
    'back':[
        ['b', 'r', 'r'],
        ['y', 'b', 'w'],
        ['b', 'r', 'r']
        ]},
    {'left':[
        ['y', 'o', 'w'],
        ['g', 'o', 'o'],
        ['y', 'b', 'w']
        ], 
    'right':[
        ['y', 'r', 'w'],
        ['b', 'r', 'r'],
        ['y', 'g', 'w']
        ]}, 
    {'top':[
        ['b', 'b', 'o'],
        ['w', 'w', 'w'],
        ['r', 'g', 'g']
        ], 
    'bot':[
        ['o', 'b', 'b'],
        ['y', 'y', 'y'],
        ['g', 'g', 'r']
        ]}
        ]
left_down = [
    {'front':[
        ['b', 'o', 'o'],
        ['w', 'g', 'w'],
        ['r', 'o', 'o']
        ],
    'back':[
        ['b', 'r', 'g'],
        ['y', 'b', 'y'],
        ['b', 'r', 'o']
        ]},
    {'left':[
        ['y', 'g', 'y'],
        ['b', 'o', 'o'],
        ['w', 'o', 'w']
        ], 
    'right':[
        ['y', 'r', 'w'],
        ['b', 'r', 'r'],
        ['y', 'g', 'w']
        ]}, 
    {'top':[
        ['r', 'b', 'o'],
        ['w', 'w', 'w'],
        ['r', 'g', 'g']
        ], 
    'bot':[
        ['g', 'b', 'b'],
        ['y', 'y', 'y'],
        ['g', 'g', 'r']
        ]}
        ]
right_up = [
    {'front':[
        ['b', 'o', 'b'],
        ['w', 'g', 'y'],
        ['r', 'o', 'r']
        ],
    'back':[
        ['g', 'r', 'g'],
        ['w', 'b', 'y'],
        ['o', 'r', 'o']
        ]},
    {'left':[
        ['y', 'g', 'y'],
        ['b', 'o', 'o'],
        ['w', 'o', 'w']
        ], 
    'right':[
        ['y', 'b', 'y'],
        ['g', 'r', 'r'],
        ['w', 'r', 'w']
        ]}, 
    {'top':[
        ['r', 'b', 'o'],
        ['w', 'w', 'w'],
        ['r', 'g', 'o']
        ], 
    'bot':[
        ['g', 'b', 'b'],
        ['y', 'y', 'y'],
        ['g', 'g', 'b']
        ]}
        ]
bot_left = [
    {'front':[
        ['b', 'o', 'b'],
        ['w', 'g', 'y'],
        ['w', 'r', 'w']
        ],
    'back':[
        ['g', 'r', 'g'],
        ['w', 'b', 'y'],
        ['w', 'o', 'w']
        ]},
    {'left':[
        ['y', 'g', 'y'],
        ['b', 'o', 'o'],
        ['r', 'o', 'r']
        ], 
    'right':[
        ['y', 'b', 'y'],
        ['g', 'r', 'r'],
        ['o', 'r', 'o']
        ]}, 
    {'top':[
        ['r', 'b', 'o'],
        ['w', 'w', 'w'],
        ['r', 'g', 'o']
        ], 
    'bot':[
        ['b', 'y', 'b'],
        ['b', 'y', 'g'],
        ['g', 'y', 'g']
        ]}
        ]

mid_left = [
    {'front':[
        ['b', 'o', 'b'],
        ['g', 'r', 'r'],
        ['w', 'r', 'w']
        ],
    'back':[
        ['g', 'r', 'g'],
        ['b', 'o', 'o'],
        ['w', 'o', 'w']
        ]},
    {'left':[
        ['y', 'g', 'y'],
        ['w', 'g', 'y'],
        ['r', 'o', 'r']
        ], 
    'right':[
        ['y', 'b', 'y'],
        ['w', 'b', 'y'],
        ['o', 'r', 'o']
        ]}, 
    {'top':[
        ['r', 'b', 'o'],
        ['w', 'w', 'w'],
        ['r', 'g', 'o']
        ], 
    'bot':[
        ['b', 'y', 'b'],
        ['b', 'y', 'g'],
        ['g', 'y', 'g']
        ]}
        ]
center_down = [
    {'front':[
        ['b', 'b', 'b'],
        ['g', 'w', 'r'],
        ['w', 'g', 'w']
        ],
    'back':[
        ['g', 'y', 'g'],
        ['b', 'y', 'o'],
        ['w', 'y', 'w']
        ]},
    {'left':[
        ['y', 'g', 'y'],
        ['w', 'g', 'y'],
        ['r', 'o', 'r']
        ], 
    'right':[
        ['y', 'b', 'y'],
        ['w', 'b', 'y'],
        ['o', 'r', 'o']
        ]}, 
    {'top':[
        ['r', 'o', 'o'],
        ['w', 'o', 'w'],
        ['r', 'r', 'o']
        ], 
    'bot':[
        ['b', 'o', 'b'],
        ['b', 'r', 'g'],
        ['g', 'r', 'g']
        ]}
        ]
mid_right = [
    {'front':[
        ['b', 'b', 'b'],
        ['w', 'g', 'y'],
        ['w', 'g', 'w']
        ],
    'back':[
        ['g', 'y', 'g'],
        ['w', 'b', 'y'],
        ['w', 'y', 'w']
        ]},
    {'left':[
        ['y', 'g', 'y'],
        ['b', 'y', 'o'],
        ['r', 'o', 'r']
        ], 
    'right':[
        ['y', 'b', 'y'],
        ['g', 'w', 'r'],
        ['o', 'r', 'o']
        ]}, 
    {'top':[
        ['r', 'o', 'o'],
        ['w', 'o', 'w'],
        ['r', 'r', 'o']
        ], 
    'bot':[
        ['b', 'o', 'b'],
        ['b', 'r', 'g'],
        ['g', 'r', 'g']
        ]}
        ]
center_up = [
    {'front':[
        ['b', 'o', 'b'],
        ['w', 'r', 'y'],
        ['w', 'r', 'w']
        ],
    'back':[
        ['g', 'r', 'g'],
        ['w', 'o', 'y'],
        ['w', 'o', 'w']
        ]},
    {'left':[
        ['y', 'g', 'y'],
        ['b', 'y', 'o'],
        ['r', 'o', 'r']
        ], 
    'right':[
        ['y', 'b', 'y'],
        ['g', 'w', 'r'],
        ['o', 'r', 'o']
        ]}, 
    {'top':[
        ['r', 'b', 'o'],
        ['w', 'g', 'w'],
        ['r', 'g', 'o']
        ], 
    'bot':[
        ['b', 'y', 'b'],
        ['b', 'b', 'g'],
        ['g', 'y', 'g']
        ]}
        ]

left_all = [
    {'front':[
        ['y', 'b', 'y'],
        ['g', 'w', 'r'],
        ['o', 'r', 'o']
        ],
    'back':[
        ['y', 'g', 'y'],
        ['b', 'y', 'o'],
        ['r', 'o', 'r']
        ]},
    {'left':[
        ['b', 'o', 'b'],
        ['w', 'r', 'y'],
        ['w', 'r', 'w']
        ], 
    'right':[
        ['g', 'r', 'g'],
        ['w', 'o', 'y'],
        ['w', 'o', 'w']
        ]}, 
    {'top':[
        ['r', 'w', 'r'],
        ['g', 'g', 'b'],
        ['o', 'w', 'o']
        ], 
    'bot':[
        ['b', 'g', 'g'],
        ['y', 'b', 'y'],
        ['b', 'b', 'g']
        ]}
        ]
up_all = [
    {'front':[
        ['b', 'g', 'g'],
        ['y', 'b', 'y'],
        ['b', 'b', 'g']
        ],
    'back':[
        ['o', 'w', 'o'],
        ['b', 'g', 'g'],
        ['r', 'w', 'r']
        ]},
    {'left':[
        ['b', 'y', 'w'],
        ['o', 'r', 'r'],
        ['b', 'w', 'w']
        ], 
    'right':[
        ['w', 'w', 'g'],
        ['o', 'o', 'r'],
        ['w', 'y', 'g']
        ]}, 
    {'top':[
        ['y', 'b', 'y'],
        ['g', 'w', 'r'],
        ['o', 'r', 'o']
        ], 
    'bot':[
        ['r', 'o', 'r'],
        ['o', 'y', 'b'],
        ['y', 'g', 'y']
        ]}
        ]
right_all = [
    {'front':[
        ['b', 'y', 'w'],
        ['o', 'r', 'r'],
        ['b', 'w', 'w']
        ],
    'back':[
        ['w', 'w', 'g'],
        ['o', 'o', 'r'],
        ['w', 'y', 'g']
        ]},
    {'left':[
        ['o', 'w', 'o'],
        ['b', 'g', 'g'],
        ['r', 'w', 'r']
        ], 
    'right':[
        ['b', 'g', 'g'],
        ['y', 'b', 'y'],
        ['b', 'b', 'g']
        ]}, 
    {'top':[
        ['y', 'r', 'o'],
        ['b', 'w', 'r'],
        ['y', 'g', 'o']
        ], 
    'bot':[
        ['y', 'o', 'r'],
        ['g', 'y', 'o'],
        ['y', 'b', 'r']
        ]}
        ]
down_all = [
    {'front':[
        ['y', 'r', 'o'],
        ['b', 'w', 'r'],
        ['y', 'g', 'o']
        ],
    'back':[
        ['r', 'b', 'y'],
        ['o', 'y', 'g'],
        ['r', 'o', 'y']
        ]},
    {'left':[
        ['r', 'b', 'o'],
        ['w', 'g', 'w'],
        ['r', 'g', 'o']
        ], 
    'right':[
        ['g', 'y', 'g'],
        ['g', 'b', 'b'],
        ['b', 'y', 'b']
        ]}, 
    {'top':[
        ['g', 'y', 'w'],
        ['r', 'o', 'o'],
        ['g', 'w', 'w']
        ], 
    'bot':[
        ['b', 'y', 'w'],
        ['o', 'r', 'r'],
        ['b', 'w', 'w']
        ]}
        ]

revers_all = [
    {'front':[
        ['r', 'b', 'y'],
        ['o', 'y', 'g'],
        ['r', 'o', 'y']
        ],
    'back':[
        ['y', 'r', 'o'],
        ['b', 'w', 'r'],
        ['y', 'g', 'o']
        ]},
    {'left':[
        ['g', 'y', 'g'],
        ['g', 'b', 'b'],
        ['b', 'y', 'b']
        ], 
    'right':[
        ['r', 'b', 'o'],
        ['w', 'g', 'w'],
        ['r', 'g', 'o']
        ]}, 
    {'top':[
        ['w', 'w', 'g'],
        ['o', 'o', 'r'],
        ['w', 'y', 'g']
        ], 
    'bot':[
        ['w', 'w', 'b'],
        ['r', 'r', 'o'],
        ['w', 'y', 'b']
        ]}
        ]
around_all = [
    {'front':[
        ['o', 'g', 'y'],
        ['r', 'w', 'b'],
        ['o', 'r', 'y']
        ],
    'back':[
        ['y', 'o', 'r'],
        ['g', 'y', 'o'],
        ['y', 'b', 'r']
        ]},
    {'left':[
        ['b', 'y', 'b'],
        ['b', 'b', 'g'],
        ['g', 'y', 'g']
        ], 
    'right':[
        ['o', 'g', 'r'],
        ['w', 'g', 'w'],
        ['o', 'b', 'r']
        ]}, 
    {'top':[
        ['w', 'w', 'b'],
        ['r', 'r', 'o'],
        ['w', 'y', 'b']
        ], 
    'bot':[
        ['w', 'w', 'g'],
        ['o', 'o', 'r'],
        ['w', 'y', 'g']
        ]}
        ]

class Test_cube(unittest.TestCase):
    def setUp(self):
        self.rub_cube = Rubik_cube()

    def rot_edge(self,row_col,side):
        pos = self.rub_cube.rotate_edge(row_col,side)
        return pos

    def rot_all(self,pos,side):
        self.rub_cube.position = pos
        pos = self.rub_cube.rotate_all(side)
        return pos

    def test_01(self):
        #test top_left
        for i,x in zip(self.rot_edge('top','left'),top_left):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("top_left"):
                        self.assertListEqual(list(k), z)
        #test right_down
        for i,x in zip(self.rot_edge('right','down'),right_down):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("right_down"):
                        self.assertListEqual(list(k), z)
        #test left_up
        for i,x in zip(self.rot_edge('left','up'),left_up):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("left_up"):
                        self.assertListEqual(list(k), z)
        #test bot_right
        for i,x in zip(self.rot_edge('bot','right'),bot_right):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("bot_right"):
                        self.assertListEqual(list(k), z)
        #test top_right
        for i,x in zip(self.rot_edge('top','right'),top_right):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("top_right"):
                        self.assertListEqual(list(k), z)
        #test left_down
        for i,x in zip(self.rot_edge('left','down'),left_down):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("left_down"):
                        self.assertListEqual(list(k), z)
        #test right_up
        for i,x in zip(self.rot_edge('right','up'),right_up):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("right_up"):
                        self.assertListEqual(list(k), z)
        #test bot_left
        for i,x in zip(self.rot_edge('bot','left'),bot_left):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("bot_left"):
                        self.assertListEqual(list(k), z)
        #test mid_left
        for i,x in zip(self.rot_edge('mid','left'),mid_left):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("mid_left"):
                        self.assertListEqual(list(k), z)
        #test center_down
        for i,x in zip(self.rot_edge('center','down'),center_down):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("center_down"):
                        self.assertListEqual(list(k), z)
        #test mid_right
        for i,x in zip(self.rot_edge('mid','right'),mid_right):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("mid_right"):
                        self.assertListEqual(list(k), z)
        #test center_up
        for i,x in zip(self.rot_edge('center','up'),center_up):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("center_up"):
                        self.assertListEqual(list(k), z)

    def test_02(self):
        #test all_left
        pos = self.rot_all(center_up,'left')
        for i,x in zip(pos,left_all):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("all_left"):
                        self.assertListEqual(list(k), z)
        #test all_up
        pos = self.rot_all(pos,'up')
        for i,x in zip(pos,up_all):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("all_up"):
                        self.assertListEqual(list(k), z)
        #test all_right
        pos = self.rot_all(pos,'right')
        for i,x in zip(pos,right_all):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("all_right"):
                        self.assertListEqual(list(k), z)
        #test all_down
        pos = self.rot_all(pos,'down')
        for i,x in zip(pos,down_all):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("all_down"):
                        self.assertListEqual(list(k), z)
        #test all_revers
        pos = self.rot_all(pos,'reverse')
        for i,x in zip(pos,revers_all):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("all_reverse"):
                        self.assertListEqual(list(k), z)
        #test all_around
        pos = self.rot_all(pos,'around')
        for i,x in zip(pos,around_all):
            for j,y in zip(i.keys(),x.keys()):
                for k,z in zip(i[j],x[y]):
                    with self.subTest("all_around"):
                        self.assertListEqual(list(k), z)

if __name__ == "__main__":
  unittest.main()