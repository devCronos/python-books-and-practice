from tkinter import *

def doNothing():
    print("NOTHING :)...")

root = Tk()
#                            **********MENU************
menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File",menu=submenu)

submenu.add_command(label="New thing", command=doNothing)
submenu.add_command(label="New powers", command=doNothing)
submenu.add_separator()
submenu.add_command(label="New aids", command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit", command=doNothing)

editmenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Neewmol thing", command=doNothing)

#                              *******TOOLBAR***********

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="idk man", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="print",command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP,fill=X)

#                               *******STATUSBAR************

status=Label(root,text="Preparing to do nothing...",bd=1, relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)



root.mainloop()