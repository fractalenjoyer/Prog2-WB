from PIL import Image
import numpy as np
from numba import jit

@jit(nopython=True)
def calc(a,b): 
    c = complex(a,b)
    z = 0
    for i in range(255):
        z = z*z + c 
        if abs(z) > 10**10:
            return i
    return 0

@jit()
def mandel():
    img = np.zeros((1000,1000,3), dtype=np.uint8)
    startx = -2
    starty = -1.5
    delta = 3/1000
    a = startx
    b = starty
    for x in range(1000):
        for y in range(1000):
            img[x,y, 0] = calc(a, b)
            b += delta
        a += delta
        b = starty
    return img

Image.fromarray(mandel()).save('mandel2.png')
