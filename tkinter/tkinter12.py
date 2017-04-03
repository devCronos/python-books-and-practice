from tkinter import *

root = Tk()

photo = PhotoImage(file="image02.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()