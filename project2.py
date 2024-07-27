from tkinter.ttk import Combobox
import ttkbootstrap as v
from tkinter.messagebox import showerror, showinfo
from PIL import ImageTk, Image

# Register form
def submit(root):
    root.destroy()
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

def submit_form(root):
    showinfo("Message", "Form submitted successfully")

def log(root, e1, e2):
    username = e1.get()
    password = e2.get()
    if username == "tamil" and password == "1234":
        showinfo("Message", "Login Successful")
    else:
        showerror("Error", "Invalid username or password")

# Login form
def click(root):
    root.destroy()
    root = v.Window(
        title="LOGIN",
        themename="cosmo",
    )
    root.geometry("600x300")
    root.title("Login form")
    image = Image.open("design1.jpg")
    image = ImageTk.PhotoImage(image)
    image_label = v.Label(root, image=image)
    image_label.pack()

    l1 = v.Label(root, text="LOGIN FROM", font=20, bootstyle="dark")
    l1.place(x=120, y=30)
    l2 = v.Label(root, text="Username:", font=20, bootstyle="info")
    l2.place(x=170, y=100)
    e1 = v.Entry(root, bootstyle="info")
    e1.place(x=260, y=100)
    l3 = v.Label(root, text="Password:", font=20, bootstyle="info")
    l3.place(x=170, y=150)
    e2 = v.Entry(root, bootstyle="info")
    e2.place(x=260, y=150)
    b1 = v.Button(root, text="L O G I N", command=lambda: log(root, e1, e2), bootstyle="success")
    b1.place(x=290, y=200)
    root.mainloop()

# Home
root = v.Window(
    title="HOME",
    themename="cosmo",
)
root.geometry("800x600")
frame = v.Frame(root, width="1000", height="40", bootstyle="light")
frame.pack()
l1 = v.Label(frame, text="Home", font=20, bootstyle="info")
l1.place(relx=0.1, rely=0.1)
l2 = v.Label(frame, text="Contact", font=20, bootstyle="info")
l2.place(relx=0.2, rely=0.1)
l3 = v.Label(frame, text="Gallery", font=20, bootstyle="info")
l3.place(relx=0.3, rely=0.1)
l4 = v.Button(frame, text="Register", command=lambda: submit(root), bootstyle="info")
l4.place(relx=0.6, rely=0.1)
l5 = v.Button(frame, text="Login", command=lambda: click(root), bootstyle="success")
l5.place(relx=0.9, rely=0.1)
root.mainloop()
