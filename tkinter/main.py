from tkinter import *

root = Tk()

lbl = Label(root)
canvas = Canvas(root, width=500, height=500)


def key_handler(event):
    if event.keysym == "BackSpace":
        lbl["text"] = lbl["text"][:-1]
    else:
        lbl["text"] += event.char

def draw(event):
    canvas.create_oval(event.x, event.y, event.x+5, event.y+5, fill="black")

def erase(event):
    canvas.create_oval(event.x-10, event.y-10, event.x+10, event.y+10, fill="white", outline="white")


root.bind('<Key>', key_handler)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<B3-Motion>", erase)
lbl.pack()
canvas.pack()
root.mainloop()