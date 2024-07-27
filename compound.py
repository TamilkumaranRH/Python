""" from tkinter import*
r=Tk()
r.config(background="yellow")
r.geometry("400x400")

def clear_all():
    principal_field.delete(0,END)
    rate_field.delete(0,END)
    time_field.delete(0,END)
    compound_field.delete(0,END)

    principal_field.focus_set()
def calculate_ci():
    principal=int(principal_field.get())
    rate=float(rate_field.get())
    time=int(time_field.get())
    CI = principal * (pow((1 + rate / 100), time))
    compound_field.insert(10,CI)

l1=Label(r,text="principal amount",bg="skyblue",fg="black",font=15)
l1.grid(row=1,column=0,padx=10,pady=10)
l2=Label(r,text="rate(%)",bg="skyblue",fg="black",font=15)
l2.grid(row=2,column=0,padx=10,pady=10)
l3=Label(r,text="time",bg="skyblue",fg="black",font=15)
l3.grid(row=3,column=0,padx=10,pady=10)
l4=Label(r,text="compound interest",bg="skyblue",fg="black",font=15)
l4.grid(row=5,column=0,padx=10,pady=10)

principal_field=Entry(r)
principal_field.grid(row=1,column=1,padx=10,pady=10)
rate_field=Entry(r)
rate_field.grid(row=2,column=1,padx=10,pady=10)
time_field=Entry(r)
time_field.grid(row=3,column=1,padx=10,pady=10)
compound_field=Entry(r)
compound_field.grid(row=5,column=1,padx=10,pady=10)

b1=Button(r,text="Submit",command=calculate_ci,bg="lime",fg="black",font=15)
b1.grid(row=4,column=1,pady=10)
b2=Button(r,text="Clear",command=clear_all,bg="lime",fg="black",font=15)
b2.grid(row=6,column=1,pady=10)
r.mainloop() """

""" import tkinter as tk
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.title("GIF Image Viewer")

    # Load the GIF file
    gif_path = "voice.gif"  # Change this to the path of your GIF file
    gif_image = Image.open(gif_path)
    gif_photo = ImageTk.PhotoImage(gif_image)

    # Create a label widget to display the GIF image
    gif_label = tk.Label(root, image=gif_photo)
    gif_label.pack()

    # Start the tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
 """




