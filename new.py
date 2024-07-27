from tkinter import *

def new1(root):
    root.destroy()
    root=Tk()
    root.mainloop()


#home page
root=Tk()
Button(root,command=lambda:new1(root)).pack()
root.mainloop()