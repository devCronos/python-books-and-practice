from tkinter import *
import tkinter.messagebox
root = Tk()

#tkinter.messagebox.showinfo('Windowww Title', 'Monkey orange')

answer = tkinter.messagebox.askyesno('Question 1','Do you even, brah ?')
if answer == "yes":
    print(" XD ")


root.mainloop()