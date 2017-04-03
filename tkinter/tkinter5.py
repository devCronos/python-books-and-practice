from tkinter import *

root = Tk()

""""def printName():
    print("Hi im Claudiu")

button_1 = Button(root,text="Me nome",command=printName)
button_1.pack()"""




def anotherName(event):
    print("Hi im Clau")

button_1 = Button(root, text="Say my name")
button_1.bind("<Button-1>",anotherName)
button_1.pack()

root.mainloop()