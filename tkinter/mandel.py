from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from numba import jit

root = Tk()
HEIGHT = 500
WIDTH = 500
mandel = Canvas(root, width=WIDTH, height=HEIGHT)


@jit(nopython=True)
def calc(a, b):
    z = c = complex(a, b)
    for i in range(1, 255):
        z = z * z + c
        if abs(z) > 2:
            return i
    return 0

# def bad():
#     for x in range(0,WIDTH,10):
#         for y in range(0,HEIGHT,10):
#             a, b = 3 * x / WIDTH - 2, 3 * y / HEIGHT - 1.5
#             color = min(calc(a, b)*10, 255)
#             mandel.create_rectangle(x-5, y-5, x+5, y+5, fill=f"#{color:02x}0000")

@jit()
def main():
    img = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            a, b = 3 * x / WIDTH - 2, 3 * y / HEIGHT - 1.5
            color = min(calc(a, b)*10, 255)
            img[x,y] = [color, 0, 0]
    img = Image.fromarray(img)
    return ImageTk.PhotoImage(img)

def draw(event):
    mandel.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="white", outline="white")

mandel.bind("<B1-Motion>", draw)

image = main()

mandel.create_image(0, 0, anchor=NW, image=image)

mandel.pack()

root.mainloop()
