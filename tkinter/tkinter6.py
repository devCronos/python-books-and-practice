from tkinter import *

root = Tk()

def lc(event):
    print("Left")

def rc(event):
    print("Right")

def mc(event):
    print("Middle")

frame = Frame(root,width=300, height=250)
frame.bind("<Button-1>", lc)
frame.bind("<Button-3>", rc)
frame.bind("<Button-2>", mc)

frame.pack()

root.mainloop()