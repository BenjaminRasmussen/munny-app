import matplotlib.pyplot as mp
import numpy

x = [[4, 1, 4, 1, 0, 4, 0, 0],
     [8, 5, 8, 5, 2, 1, 0, 0],
     [9, 14, 20, 10, 9, 7, 3, 3],
     [15, 10, 10, 13, 8, 3, 2, 1],
     [6, 0, 5, 4, 4, 2, 1, 3]]
newx = [[4, 8, 9, 15, 6],
        [1, 5, 14, 10, 0],
        [4, 8, 20, 10, 4],
        [1, 5, 10, 13, 4],
        [0, 2, 9, 8, 2],
        [4, 1, 9, 8, 1],
        [0, 0, 7, 3, 1],
        [0, 0, 3, 1, 3]
        ]
y = [[1] * 8, [2] * 8, [3] * 8, [4] * 8, [5] * 8]

mp.scatter(y, x)
mp.title("Happiness Versus Exercise")
mp.xscale("linear")
mp.yscale("linear")
mp.yticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# Just for appearance's sake
mp.axis('tight')
mp.xticks([1, 2, 3, 4, 5])
mp.ylabel("Exercise in hours")
mp.xlabel("Happiness, ascending")
mp.show()
