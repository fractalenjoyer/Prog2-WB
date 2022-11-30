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
    root.config(cursor="")
    canvas.create_oval(event.x, event.y, event.x+5, event.y+5, fill="black")

def erase(event):
    root.config(cursor="spraycan")
    object = canvas.find_closest(event.x, event.y)
    try:
        coords = canvas.coords(object[0])
    except IndexError:
        return
    if (coords[0] - event.x)**2 + (coords[1] - event.y)**2 < 400:
        canvas.delete(object[0])

    



root.bind('<Key>', key_handler)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<B3-Motion>", erase)
lbl.pack()
canvas.pack()
root.mainloop()