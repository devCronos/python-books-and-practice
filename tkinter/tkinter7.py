from tkinter import *

root = Tk()


class ClauButtons:
    def __init__(self, master):
        frame=Frame(master)
        frame.pack()

        self.printButton = Button(frame,text="print message", command = self.printMessage)
        self.printButton.pack(side=LEFT)
        self.quitButton = Button(frame,text="quit",command = frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("wooow it worked")


c = ClauButtons(root)
root.mainloop()