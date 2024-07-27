from tkinter import *
from tkinter import font
import requests
from PIL import ImageTk,Image

def get_live_train_status(trainno):
    base_url = "https://rappid.in/apis/train.php?train_no={}".format(trainno)
    response = requests.get(base_url)
    data = response.json()
    return data

def fetch_train_status():
    root=Tk()
    root.geometry("700x500")
    train_number = entry_train_number.get()
    train_status = get_live_train_status(train_number)
    if "error" in train_status:
        status_text.set("Error: " + train_status["error"])
    else:
        status_text.set("Train Name: " + train_status["train_name"])

        print("*****************************************************************************")
   
        l1=Label(root,text="\t\tTrain Name : "+train_status["train_name"],font=label_font)
        l1.place(x=30,y=30)
        print("*****************************************************************************")
        for station_info in train_status["data"]:
          

          if station_info["is_current_station"]:
             l2=Label(root,text="Now Station \t\t\t\t: "+station_info["station_name"],font=label_font)
             l2.place(x=30,y=60)
             l3=Label(root,text="Distance From the Starting \t: "+station_info["distance"],font=label_font)
             l3.place(x=30,y=90)
             l4=Label(root,text="Timing \t\t\t\t\t\t: "+station_info["timing"],font=label_font)
             l4.place(x=30,y=120)
             l5=Label(root,text="Delay \t\t\t\t\t\t: "+station_info["delay"],font=label_font)
             l5.place(x=30,y=150)
             l6=Label(root,text="Platform No \t\t\t\t: "+station_info["platform"],font=label_font)
             l6.place(x=30,y=180)
             l7=Label(root,text="Halt Timing \t\t\t\t: "+station_info["halt"],font=label_font)
             l7.place(x=30,y=210)
          else:
              
            l8=Label(root,text="Now Station \t\t\t\t: "+station_info["station_name"],font=label_font)
            l8.place(x=30,y=240)
            print("*****************************************************************************")
            l9=Label(root,text="\t\tMessage \t\t: "+train_status["message"],font=label_font)
            l9.place(x=30,y=270)
            l0=Label(root,text="\t\tMessage Updated : "+train_status["updated_time"],font=label_font)
            l0.place(x=30,y=300)
            print("*****************************************************************************")

# Create the main window
root = Tk()
root.title("TRAIN")
root.geometry("700x500")
frame=Frame(root,width=2000,height=60,bg="black")
frame.pack()
label_font=font.Font(weight="bold",family="Times New Roman",size=30)
x=Label(frame,text="Train Status",font=label_font,bg="black")
x.config( fg= "white")
x.place(relx=0.43,rely=0.01)

frame=Frame(root,height=800,width=800)
frame.pack()
frame.place(anchor="center",x=650,y=450)
img=ImageTk.PhotoImage(Image.open("train2.jpg"))
label=Label(frame,image = img,width=1300)
label.pack()

# Create input elements
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
label_train_number = Label(root, text="Enter Train Number:",font=label_font,fg="black")
label_train_number.place(x=190,y=450)
entry_train_number = Entry(root,font=label_font)
entry_train_number.place(x=450,y=450)

button_get_status =Button(root, text="Get Status", command=fetch_train_status,font=label_font)
button_get_status.place(x=310,y=550)
button_get_status.config(bg="green")

# Create a label to display status
status_text = StringVar()
label_status =Label(root, textvariable=status_text, wraplength=300,font=label_font)
label_status.place(x=320,y=650)

root.mainloop()



