from tkinter import font
import pyttsx3

def  main1():
    engine=pyttsx3.init()
    engine.setProperty('rate',100)
    engine.setProperty('volume',1.0)
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.say(t.get("1.0",END))
    engine.runAndWait()
    engine.stop()

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.geometry('700x500')
frame=Frame(root,width=2000,height=60,bg="black")
frame.pack()
label_font=font.Font(weight="bold",family="Times New Roman",size=30)
x=Label(frame,text="Speech Recognition",font=label_font,bg="black")
x.config( fg= "white")
x.place(relx=0.43,rely=0.01)

frame=Frame(root,height=300,width=1000)
frame.pack()
frame.place(anchor="center",x=650,y=527)
img=ImageTk.PhotoImage(Image.open("voice.gif"))
label=Label(frame,image = img)
label.pack()

label_font = font.Font(weight="bold",family='Times New Roman',size=10)
t= Text(root,height=2, width=12)
t.place(x= 100,y=80)

label_font = font.Font(weight="bold",family='Times New Roman',size=15)
b=Button(root,text="Text to Speak",bg="skyblue",command=lambda:main1(),font=label_font)
b.place(x= 100,y=130)
root.mainloop()


#GIFimages tk
""" import tkinter as tk
from PIL import Image, ImageTk

class AnimatedGIFLabel(tk.Label):
    def __init__(self, master, path):
        self.gif = Image.open(path)
        self.frames = []
        self._load_frames()
        self.idx = 0
        super().__init__(master)
        self._animate()

    def _load_frames(self):
        try:
            while True:
                self.frames.append(ImageTk.PhotoImage(self.gif.copy()))
                self.gif.seek(len(self.frames))
        except EOFError:
            pass

    def _animate(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.after(100, self._animate)

def main():
    root = tk.Tk()
    root.title("Animated GIF Viewer")

    # Load the animated GIF file
    gif_path = "voice.gif"  # Change this to the path of your animated GIF file

    # Create an AnimatedGIFLabel instance to display the animated GIF
    gif_label = AnimatedGIFLabel(root, gif_path)
    gif_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main() """