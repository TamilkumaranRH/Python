from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image

root=Tk()
root.geometry("500x500")
root.config(background="white")
frame=Frame(root,height=200,width=200)
frame.pack()
frame.place(anchor="n",relx=0.5)

img=ImageTk.PhotoImage(Image.open("kitkat.jpg"))
label=Label(frame,image = img)
label.pack()

l1=Label(root,text="firstname:")
l1.place(relx=0.05,rely=0.5)
l2=Label(root,text="lastname:")
l2.place(relx=0.05,rely=0.6)
l1=Entry(root)
l1.place(relx=0.2,rely=0.5)
l2=Entry(root)
l2.place(relx=0.2,rely=0.6)

l3=Label(root,text="Gender:")
l3.place(relx=0.5,rely=0.5)
var=IntVar()
r1=Radiobutton(root,text="Male",variable=var,value=1)
r1.place(relx=0.6,rely=0.5)
r2=Radiobutton(root,text="Female",variable=var,value=2)
r2.place(relx=0.7,rely=0.5)

l4=Label(root,text="country:")
l4.place(relx=0.5,rely=0.6)
combo = ttk.Combobox(root, values=["India", "America", "Africa"])
combo.place(relx=0.6,rely=0.6)

text1=Label(root,text="Message : ")
text1.place(relx=0.5,rely=0.7)
text2 = Text(root,height=2, width=18)
text2.place(relx=0.6,rely=0.7)

def align(name):
    messagebox.showwarning("Excellent work",name)
B1=Button(root,text="Done",command=lambda:align(l1.get()))
B1.place(relx=0.7,rely=0.9)
root.mainloop()

import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Create a tkinter window
root = tk.Tk()
root.title("Combobox Example")

# Create a style using ttkbootstrap
style = Style(theme='flatly')

# Define a Combobox
combobox = ttk.Combobox(root, style="TCombobox", values=["Option 1", "Option 2", "Option 3"])
combobox.pack(padx=10, pady=10)

# Run the tkinter event loop
root.mainloop()
