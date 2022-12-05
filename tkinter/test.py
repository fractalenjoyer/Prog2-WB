import numpy as np
test = np.arange(100).reshape(10, 10)
coord = (5,5)
test[coord[0]-1:coord[0]+2, coord[1]-1:coord[1]+2] += 1
print(test)