import unittest
import numpy as np

class BoardTest( unittest.TestCase):

    def test1Alive(self):
        g = np.array( [[1, 0, 0],[ 0, 1, 0],[ 0, 0, 1]] )
        x,y =  1,1
        result = calcNewAlive( g, x,y)
        self.assertEqual( result, 1)

    def test2Alive( self):
        g = np.array( [[1, 0, 0],[ 0, 0, 0],[ 0, 0, 1]] )
        x,y =  1,1
        result = calcNewAlive( g, x,y)
        self.assertEqual( result, 0)

    def test1Board(self):
        g = np.array( [[0, 0, 0, 0],[ 0, 1,1, 0],[ 0, 1,1, 0],[ 0, 0, 0,0]] )
        result = calcNewBoard( g)
        self.assertTrue(np.array_equal(g, result))

    def test2Board(self):
        g = np.array( [[0, 0, 0, 0, 0],[ 0, 0, 1,0, 0],[ 0, 0, 1,0, 0],[ 0, 0, 1,0, 0],[0, 0, 0, 0, 0]] )
        gOut = np.array( [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0]])
        result = calcNewBoard( g)
        self.assertTrue(np.array_equal(gOut, result))

def calcNewAlive( board, x,y):
    currentState = board[y,x]
    subBoard = board[y-1:y+2, x-1:x+2]
    neighborsAlive = np.sum( subBoard) - board[y,x]

    if currentState == 0 and neighborsAlive == 3:
        return 1
    if currentState == 1 and (neighborsAlive == 2 or neighborsAlive ==3):
        return 1
    return 0

def calcNewBoard( board):
    newBoard = np.zeros( board.shape)
    for y in range(1,board.shape[0]):
        for x in range(1,board.shape[1]):
            newBoard[y,x] = calcNewAlive(board,x,y)

    return newBoard #np.zeros(board.size)





if __name__ == '__main__':
    unittest.main()
