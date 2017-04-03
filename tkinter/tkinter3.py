from tkinter import *

root = Tk()

one = Label(root, text='onee', bg='red',  fg='white')
one.pack()
two = Label(root, text='twoo', bg='green',  fg='black')
two.pack(fill=X)
three = Label(root, text='threeee', bg='white',  fg='black')
three.pack(side=LEFT, fill=Y)





root.mainloop()