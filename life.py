
import numpy as np




def test1( g):
    # print(g)
    # g[1,1]= 0
    state = g[1,1]
    total = np.sum(g)
    if state == 1 and (total-state) == 1:
        return 1
    else
        return 0





# make basic zero grid
grid1 = np.zeros((3,3))
grid1[0,0] = 1
grid1[1,1] = 1


# run test 1
res = test1( grid1 )

print grid1
