from tkinter import *

root = Tk()

canvas = Canvas(root,width=200,height=100)
canvas.pack()

blackline = canvas.create_line(0,0, 130,80)
redline = canvas.create_line(0,100,180,30, fill="red", width=5)
greenbox = canvas.create_rectangle(40,15,130,60, fill="green")

canvas.delete(redline)
#canvas.delete(ALL)

root.mainloop()