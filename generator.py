""" def hello():
    n=1
    while n<14:
        val=n*n
        yield val
        n+=3

a=hello()
for i in a:
    print(i) """
""" from tkinter.ttk import Combobox
import ttkbootstrap as v
root = v.Window(
        title="REGISTER",
        themename="simplex",
    )
root.geometry("900x400")
root.title("Register form")
frame = v.Frame(root, width="800", height="600", bootstyle="solar")
frame.pack()
l1 = v.Label(frame, text="Firstname:", font=20,bootstyle="info")
l1.place(x=170, y=100)
l2 = v.Label(frame, text="Lastname:", font=20,bootstyle="info")
l2.place(x=170, y=150)
e1 = v.Entry(frame)
e1.place(x=260, y=100)
e2 = v.Entry(frame)
e2.place(x=260, y=150)

l3 = v.Label(frame, text="Gender:", font=20, bootstyle="info")
l3.place(x=170, y=200)
from tkinter import IntVar, Radiobutton
from tkinter import ttk
var = IntVar()
r1 = Radiobutton(frame, text="Male", variable=var, value=1)
r1.place(x=260, y=200)
r2 = Radiobutton(frame, text="Female", variable=var, value=2)
r2.place(x=350, y=200)
l4 = v.Label(frame, text="country:", font=20,bootstyle="info")
l4.place(x=170, y=250)
combobox = ttk.Combobox(frame, values=["Option 1", "Option 2", "Option 3"],bootstyle="danger")
combobox.place(x=260, y=250)

from tkinter import Button
b2 = Button(frame, text="S U B M I T", font=20,)
b2.place(x=360, y=300)
root.mainloop() """

import ttkbootstrap as v

root = v.Window(
    title="REGISTER",
    themename="simplex",
)
root.geometry("900x400")
root.title("Register form")
frame = v.Frame(root, width="800", height="600", bootstyle="solar")
frame.pack()
l1 = v.Label(frame, text="firstname:", font=20)
l1.place(x=170, y=100)
l2 = v.Label(frame, text="lastname:", font=20)
l2.place(x=170, y=150)
e1 = v.Entry(frame)
e1.place(x=260, y=100)
e2 = v.Entry(frame)
e2.place(x=260, y=150)

l3 = v.Label(frame, text="Gender:", font=20, bootstyle="info")
l3.place(x=170, y=200)
from tkinter import IntVar, Radiobutton
from tkinter import ttk
var = IntVar()
r1 = Radiobutton(frame, text="Male", variable=var, value=1)
r1.place(x=260, y=200)
r2 = Radiobutton(frame, text="Female", variable=var, value=2)
r2.place(x=350, y=200)

l4 = v.Label(frame, text="country:", font=20)
l4.place(x=170, y=250)
combobox = ttk.Combobox(frame, values=["Option 1", "Option 2", "Option 3"],bootstyle="danger")
combobox.place(x=260, y=250)

from tkinter import Button
b2 = Button(frame, text="S U B M I T", font=20, command=lambda: submit_form(root))
b2.place(x=360, y=300)
root.mainloop()