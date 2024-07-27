from tkinter import*
t=Tk()
t.geometry("600x600")
frame=Frame(t,bg="skyblue")
frame.pack()
l1=Label(frame,text="first number",font=15,bg="skyblue")
l1.grid(row=0,column=1)
l2=Label(frame,text="second number",font=15,bg="skyblue")
l2.grid(row=1,column=1)
l1=Label(frame,text="result",font=15,bg="skyblue")
l1.grid(row=2,column=1)

e1=Entry(frame)
e1.grid(row=0,column=2)
e2=Entry(frame)
e2.grid(row=1,column=2)
e3=Entry(frame)
e3.grid(row=2,column=2)

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    e3.delete(0,20)
    e3.insert(0,c)

def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    e3.delete(0,20)
    e3.insert(0,c)

def multiply():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    e3.delete(0,20)
    e3.insert(0,c)

def divide():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    e3.delete(0,20)
    e3.insert(0,c)     

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

b1=Button(frame,text="Add",command=lambda:add(),activebackground="lime")
b1.grid(row=4,column=1)
b2=Button(frame,text="Subract",command=lambda:sub(),activebackground="lime")
b2.grid(row=4,column=2)
b3=Button(frame,text="Multiple",command=lambda:multiply(),activebackground="lime")
b3.grid(row=4,column=5)
b4=Button(frame,text="Division",command=lambda:divide(),activebackground="lime")
b4.grid(row=4,column=7)

b5=Button(frame,text="clear",command=lambda:clear())
b5.grid(row=5,column=6)
t.mainloop() 

from tkinter import*
root=Tk()
text=Text(root,height=5,width=20,font=35)
text.pack(padx=35,pady=25)
b=Button(root,text="Submit")
b.pack()
text.insert(INSERT,"HELLO")
text.insert(END,"WORLD")
text.tag_add("start","1.0", "1.4")
text.tag_add("end","1.6","1.9")
text.tag_config("start",background="red",foreground="yellow")
text.tag_config("end",background="orange",foreground="yellow")

root.mainloop()


from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Combobox")
root.geometry('300x300')
combo = ttk.Combobox(root, values=["NAME", "AGE", "SALARY"])
combo.pack()
combo1 = ttk.Combobox(root)
combo1.pack()

def option_selected(event):
   selected_option = combo.get()
   if selected_option=="NAME":
         combo1.config(values=["raja","arun"])
   elif selected_option=="AGE":
         combo1.config(values=["18","20"])
   elif selected_option=="SALARY":
         combo1.config(values=["20000","30000"])
         
   print("You selected:", selected_option)
   
combo.bind("<<ComboboxSelected>>", option_selected)
root.mainloop() 

from tkinter import*
def sel():
    selection="selected option is:"+str(var.get())
    l1.config(text=selection)
root=Tk()
var=IntVar()
r1=Radiobutton(root,text="option1",variable=var,value=1,command=sel)
r1.pack()
r2=Radiobutton(root,text="option2",variable=var,value=2,command=sel)
r2.pack()
r3=Radiobutton(root,text="option3",variable=var,value=3,command=sel)
r3.pack()
l1=Label(root)
l1.pack()
root.mainloop()

"""from tkinter import*
from PIL import Image
from PIL.ImageTk import PhotoImage
top=Tk()
top.geometry("500x500")
img= PhotoImage(Image.open("image4.jpg"))
label=Button(top,image=img).pack()
top.mainloop()"""
