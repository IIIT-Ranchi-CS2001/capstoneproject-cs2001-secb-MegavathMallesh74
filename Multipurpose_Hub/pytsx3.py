from tkinter import *
import pyttsx3 #type:ignore

root=Tk()

engine = pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

obj=LabelFrame(root,text="Text to speech",font=20,bd=1,bg="lightblue1",fg="black")
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Text",font=30,bg="lightblue1")
lbl.pack(side=LEFT)

textv=StringVar()

text=Entry(obj,textvariable=textv,font=30,width=35,bd=5)
text.pack(side=LEFT,padx=10)

Btn=Button(obj,text="Speak",bg="crimson",fg="white",bd=3,command=speaknow)
Btn.pack(side=LEFT,padx=15)

root.title("Text to Speech")
root.geometry("600x200")
root.mainloop()


