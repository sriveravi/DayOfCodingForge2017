import unittest
import numpy as np
import copy

# class LifeGame():
#     __init__(self):
#         self.gameBoard =
DEAD = 0
ALIVE = 1
ZOMBIE = 2

def getNeighbors( board,y,x):
    neighbors = []
    for y1 in range(-1,2):
        for x1  in range(-1,2):
            if x1 == 0 and y1 == 0:
                pass
            elif x + x1 < 0 or x + x1 >= board.shape[1]:
                pass
            elif y + y1 < 0 or y + y1 >= board.shape[0]:
                pass
            else:
                neighbors.append(board[y+y1,x+x1])
    return neighbors

def nextCellState(board,y,x):
    currState = board[y,x]
    neighbors = getNeighbors( board, y,x)

    # Zombie cases
    if isZombie(currState):
        if not hasLive( neighbors):
            return DEAD
        elif hasLive( neighbors):
            return ZOMBIE

    # Dead cases
    if isDead( currState):
        if zombiePlayground(neighbors):
            return ZOMBIE
        elif fertile(neighbors):
            return ALIVE

    return DEAD

def fertile( neighbors):
    return len(liveNeighbors(neighbors)) == 3

def zombiePlayground(neighbors):
    return (len(liveNeighbors(neighbors))+ len(zombieNeighbors(neighbors)) )==4


def liveNeighbors( neighborList):
    return [val for val in neighborList if val == ALIVE  ]

def zombieNeighbors( neighborList):
    return [val for val in neighborList if val == ZOMBIE  ]

def isZombie(state):
    return state == ZOMBIE

def isAlive( state):
    return state == ALIVE

def isDead( state):
    return state == DEAD


def hasLive( neighborList):
    return len( liveNeighbors(neighborList)) >0


class TestGrid(unittest.TestCase):

    # def test_Something(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    def testZombieStarving(self):
        g = np.zeros( (3,3))
        g[1,1] = ZOMBIE
        nextState = nextCellState(g, 1,1)
        self.assertEqual( nextState, DEAD)

    def testZombieFeeding(self):
        g = np.zeros( (3,3))
        g[1,1] = ZOMBIE
        g[0,0] = ALIVE
        nextState = nextCellState(g, 1,1)
        self.assertEqual( nextState, ZOMBIE)

    def testSpontaneousZombie( self):
        g = np.array([[1,1,1],[1,0,0],[0,0,0]])
        nextState = nextCellState(g, 1,1)
        self.assertEqual( nextState, ZOMBIE)

    def testBecomeAlive( self):
        g = np.array([[1,1,1],[0,0,0],[0,0,0]])
        nextState = nextCellState(g, 1,1)
        self.assertEqual( nextState, ALIVE)

    # def testGetNeighbors(self):
    #     g = np.ones( (3,3))
    #     n = [1,1,1, ])

if __name__ == '__main__':
    unittest.main()

# 0: dead
# 1: alive
# 2: zombie
