import tkinter
from tkinter import *
from tkinter import ttk, font, messagebox


#admin login
def click(root):
    root.destroy()
    root=Tk()
    root.geometry("600x300")
    root.config(bg="orange")
    root.title("Admin Login")
    frame=Frame(root,width=1800,height=40,bg="blue")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    x=Label(frame,text="IFC BANK",font=label_font,)
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.43,rely=0.01)

    frame=Frame(root,width=700,height=350,bg="yellow")
    frame.pack()
    frame.place(relx=0.3,rely=0.3)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(frame,text="ADMIN LOGIN ",font=label_font)
    l1.place(x=120,y=30)
    l1.config(bg="yellow")

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l2=Label(frame,text="Adminname:",font=label_font)
    l2.place(x=170,y=100)
    l2.config(bg="yellow")
    e1=Entry(frame,font=label_font)
    e1.place(x=360,y=100)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l3=Label(frame,text="Password:",font=label_font)
    l3.place(x=170,y=150)
    l3.config(bg="yellow")
    e2=Entry(frame,font=label_font)
    e2.place(x=360,y=150)

    b1=Button(frame,text="L O G I N",command=lambda:log(root,e1,e2),font=label_font)
    b1.place(x=290,y=250)
    b1.config(bg="green")

    frame1=Frame(root,width=1700,height=40,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame1,text="Copyright © 2024 IFC ",font=label_font,bg="Red")
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.39,rely=0.01)
    frame1.place(relx=0.0004,rely=0.95)
    root.mainloop()


def log(root,e1,e2):
    Adminname=e1.get()
    Password=e2.get()
    if Adminname=="tamil" and Password=="1234":
        messagebox.showinfo("Successfully login")

    else:
         messagebox.showerror( "Incorrect", "Invalid Adminname and Password")




#customer login
def next(root):
    root.destroy()
    root=Tk()
    root.title("customer login")
    root.geometry("600x400")
    root.config(bg="yellow")
    frame=Frame(root,width=1800,height=40,bg="blue")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    x=Label(frame,text="IFC BANK",font=label_font,)
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.43,rely=0.01)

    frame=Frame(root,width=700,height=350,bg="skyblue")
    frame.pack()
    frame.place(relx=0.3,rely=0.3)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(frame,text="LOGIN",font=label_font,bg="skyblue")
    l1.place(x=120,y=30)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l2=Label(frame,text="Customer ID:",font=label_font,bg="skyblue")
    l2.place(x=170,y=100)
    e1=Entry(frame,font=label_font)
    e1.place(x=390,y=100)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l3=Label(frame,text="Customer name:",font=label_font,bg="skyblue")
    l3.place(x=170,y=150)
    e2=Entry(frame,font=label_font)
    e2.place(x=390,y=150)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l3=Label(frame,text="Amount deposit:",font=label_font,bg="skyblue")
    l3.place(x=170,y=200)
    e3=Entry(frame,font=label_font)
    e3.place(x=390,y=200)

    def next(root):
         Customer_ID=e1.get()
         Customer_name=e2.get()
         Amount_deposit=e3.get()
         f=open("bank.txt","a")
         f.write("\n"+str(Customer_ID)+"\t"+Customer_name+"\t"+Amount_deposit)

    b1=Button(frame,text="S U B M I T",command=lambda:next(root),font=label_font)
    b1.place(x=400,y=270)
    b1.config(bg="green")

            
    frame1=Frame(root,width=1700,height=40,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame1,text="Copyright © 2024 IFC ",font=label_font,bg="Red")
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.39,rely=0.01)
    frame1.place(relx=0.0004,rely=0.95)

#customer register
def back(root):
    root.destroy()
    root=Tk()
    root.title("customer login")
    root.geometry("600x400")
    root.config(bg="gray")
    frame=Frame(root,width=1800,height=40,bg="blue")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    x=Label(frame,text="IFC BANK",font=label_font,)
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.43,rely=0.01)

    frame=Frame(root,width=700,height=350,bg="pink")
    frame.pack()
    frame.place(relx=0.3,rely=0.3)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(frame,text="REGISTER",font=label_font,bg="pink")
    l1.place(x=120,y=30)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l2=Label(frame,text="Customer ID:",font=label_font,bg="pink")
    l2.place(x=170,y=100)
    e1=Entry(frame,font=label_font)
    e1.place(x=390,y=100)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l3=Label(frame,text="Customer name:",font=label_font,bg="pink")
    l3.place(x=170,y=150)
    e2=Entry(frame,font=label_font)
    e2.place(x=390,y=150)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l3=Label(frame,text="Amount deposit:",font=label_font,bg="pink")
    l3.place(x=170,y=200)
    e3=Entry(frame,font=label_font)
    e3.place(x=390,y=200)

    b1=Button(frame,text="S U B M I T",command=lambda:next(root),font=label_font)
    b1.place(x=400,y=270)
    b1.config(bg="green")


#home page 
root=Tk()
root.geometry("800x600")
root.config(bg="pink")
frame=Frame(root,width="1900",height="40",bg="blue")
frame.pack()
label_font=font.Font(weight="bold",family="Times New Roman",size=30)
x=Label(frame,text="IFC BANK",font=label_font,bg="pink")
x.config(bg= "blue", fg= "white")
x.place(relx=0.43,rely=0.01)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
s="""A bank is a financial institution that accepts deposits from the public
 and creates a demand deposit while simultaneously making loans.
 Lending activities can be directly performed by the bank or indirectly through capital markets."""
l=Label(root,text=s,font=label_font,bg="pink")
l.place(relx=0.1,rely=0.1)

label_font=font.Font(weight="bold",family="Times New Roman",size=20)
frame=Frame(root,width="95",bg="pink")
frame.place(relx=0.0,rely=0.0)
l1=Label(root,text="Home",font=label_font,bg="pink",fg="black")
l1.place(relx=0.0,rely=0.1)
l2=Label(root,text="Contact",font=label_font,bg="pink",fg="black")
l2.place(relx=0.0,rely=0.3)
l3=Label(root,text="Gallery",font=label_font,bg="pink",fg="black")
l3.place(relx=0.0,rely=0.5)
l4=Label(root,text="AboutUs",font=label_font,bg="pink",fg="black")
l4.place(relx=0.0,rely=0.7)

l4=Button(root,text="Customer login",command=lambda:next(root),font=label_font)
l4.place(relx=0.3,rely=0.7)
l4.config(bg="lime")

l5=Button(root,text="Customer Registeration",font=label_font,command=lambda:back(root))
l5.place(relx=0.6,rely=0.7)
l5.config(bg="lime")


label_font=font.Font(weight="bold",family="Times New Roman",size=20)
q="""A person or entity that maintains an account and/or has business relationships with the bank.
One on whose behalf the account is maintained.
The beneficiary of the transaction carried professional intermediaries."""
l=Label(root,text=q,font=label_font,bg="pink")
l.place(relx=0.1,rely=0.4)
l5=Button(root,text="Admin Login",command=lambda:click(root),font=label_font)
l5.place(relx=0.4,rely=0.3)
l5.config(bg="lime")


frame_bottom=Frame(root,width="1700",height="40",bg="blue") 

label_font=font.Font(weight="bold",family="Times New Roman",size=20)
x=Label(frame_bottom,text="Copyright © 2024 IFC ",font=label_font,bg="Red")
x.config(bg= "blue", fg= "white")
x.place(relx=0.43,rely=0.01)
frame_bottom.place(relx=0.0004,rely=0.95)
root.mainloop()