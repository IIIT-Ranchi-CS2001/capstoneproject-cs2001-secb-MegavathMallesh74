# import pikepdf  # type: ignore

# old_pdf=pikepdf.Pdf.open("hi.pdf")

# no_extr=pikepdf.Permissions(extract=False)

# old_pdf.save("new_pdf",encryption=pikepdf.Encryption(user="bongu",
#                                                       owner="bongu",
#                                                      allow=no_extr))

from tkinter import *
from datetime import date

root=Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Age Calculator")

photo=PhotoImage(file="ageimage.png")
myImage=Label(image=photo)
myImage.pack(padx=15,pady=15)

Label(text="Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Date",font=23).place(x=200,y=400)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dateValue=StringVar()

nameEntry=Entry(textvariable=nameValue,width=30,bd=3)
yearEntry=Entry(textvariable=yearValue,width=30,bd=3)

monthEntry=Entry(textvariable=monthValue,width=30,bd=3)
dateEntry=Entry(textvariable=dateValue,width=30,bd=3)

nameEntry.place(x=300,y=250)
yearEntry.place(x=300,y=300)

monthEntry.place(x=300,y=350)
dateEntry.place(x=300,y=400)  

def CalculateAge():
    today = date.today()
    current_day = today.day
    current_month = today.month
    current_year = today.year

    birth_day =  int(dateEntry.get())
    birth_month =  int(monthEntry.get())
    birth_year = int(yearEntry.get())
    
        # Initial age calculation
    age = current_year - birth_year

    # Adjust age if the current date is before the birthday this year
    if (current_month < birth_month) or (current_month == birth_month and current_day < birth_day):
        age -= 1

    # Optional: Calculate months and days
    months = current_month - birth_month
    if months < 0:
        months += 12

    days = current_day - birth_day
    if days < 0:
        # Get days in the previous month
        previous_month = current_month - 1 if current_month > 1 else 12
        previous_month_year = current_year if current_month > 1 else current_year - 1
        days_in_previous_month = (date(previous_month_year, previous_month + 1, 1) - date(previous_month_year, previous_month, 1)).days
        days += days_in_previous_month
        months -= 1

 


     
    Label(text=f"{nameValue.get()}   your   age   is   {age} years {months} months {days} days",font=50).place(x=300,y=500)

Button(text='Calculate Age',font=20,bg="black",fg="white",height=2,command=CalculateAge).place(x=300,y=450)
root.mainloop()

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


# from tkinter import *
# from tkinter import filedialog
# from tkinter import messagebox
# from PyPDF2 import PdfFileWriter,PdfFileReader

# import os

 


# root=Tk()
# root.title("Password Protector")
# root.geometry("500x600")

 


# icon_image=PhotoImage(file="image_icon.png")
# root.iconphoto(False,icon_image)

# Top_image=PhotoImage(file="Top_image.png")
# Label(root,image=Top_image).pack()

# frame=Frame(root,width=580,height=290,bd=5,relief=GROOVE)
# frame.place(x=5,y=180)

# source=StringVar()
# Label(frame,text="Source PDF",font="arial 10 bold",fg="#4c4542").place(x=10,y=50)
# entry1=Entry(frame,width=30,textvariable=source,font="arial 15",bd=1)
# entry1.place(x=100,y=50)

# def browse():
#     filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image File",filetype=(('PDF File','*.pdf'),('all files','*.*')))
#     entry1.insert(END,filename)

# def Protect():
#     mainfile=source.get()
#     protectfile=target.get()
#     code=password.get()

#     if mainfile=="" and protectfile=="" and password.get()=="":
#         messagebox.showerror("Invalid","All entries are empty!!")
#     elif mainfile=="":
#         messagebox.showerror("Invalid","Please type source Pdf filename")
#     elif protectfile=="":
#         messagebox.showerror("Invalid","Please Type Target PDF filename!!")
#     elif password.get()=="":
#         messagebox.showerror("Invalid","Please type Password")
#     else:
#         try:
#             out=PdfFileWriter()
#             file=PdfFileReader(filename)
#             num=file.numPages

#             for idx in range(num):
#                page=file.getPage(idx)
#                out.addPage(page)
#           #password
#             out.encrypt(code)
        
#             with open(protectfile,"wb") as f:
#                out.write(f)
        
#         except:
#             messagebox.showerror("Invalid","Invalid Entry!!")


# Button_icon=PhotoImage(file="button-Icon.png")
# Button(frame,image=Button_icon,height=24,width=25,command=browse).place(x=445,y=48)

# target=StringVar()
# Label(frame,text="Target PDF",font="arial 10 bold",fg="#4c4542").place(x=10,y=100)
# entry2=Entry(frame,width=30,textvariable=target,font="arial 15",bd=1)
# entry2.place(x=100,y=100)

# password=StringVar()
# Label(frame,text="Set Password",font="arial 10 bold",fg="#4c4542").place(x=10,y=150)
# entry2=Entry(frame,width=30,textvariable=password,font="arial 15",bd=1)
# entry2.place(x=100,y=150)



# button_icon=PhotoImage(file="button-Icon.png")
# Protect=Button(root,text="Protect PDF Files:",compound=LEFT,image=button_icon,width=230,height=50,bg="#bfb9b9",command=Protect)
# Protect.pack(side=BOTTOM,pady=40)


# root.mainloop()

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfWriter, PdfReader  # type: ignore

import os

root = Tk()
root.title("Password Protector")
root.geometry("500x600")

# Icon and Top Image
try:
    icon_image = PhotoImage(file="image_icon.png")
    root.iconphoto(False, icon_image)
except:
    print("Icon image not found!")

try:
    Top_image = PhotoImage(file="Top_image.png")
    Label(root, image=Top_image).pack()
except:
    print("Top image not found!")

# Frame for Inputs
frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE)
frame.place(x=5, y=180)

source = StringVar()
Label(frame, text="Source PDF", font="arial 10 bold", fg="#4c4542").place(x=10, y=50)
entry_source = Entry(frame, width=30, textvariable=source, font="arial 15", bd=1)
entry_source.place(x=100, y=50)

def browse():
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select PDF File",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
    )
    source.set(filename)

Button_icon = PhotoImage(file="button-Icon.png")
Button(frame, image=Button_icon, height=24, width=25, command=browse).place(x=445, y=48)

target = StringVar()
Label(frame, text="Target PDF", font="arial 10 bold", fg="#4c4542").place(x=10, y=100)
entry_target = Entry(frame, width=30, textvariable=target, font="arial 15", bd=1)
entry_target.place(x=100, y=100)

password = StringVar()
Label(frame, text="Set Password", font="arial 10 bold", fg="#4c4542").place(x=10, y=150)
entry_password = Entry(frame, width=30, textvariable=password, font="arial 15", bd=1)
entry_password.place(x=100, y=150)

def protect():
    mainfile = source.get()
    protectfile = target.get()
    code = password.get()

    if not mainfile or not protectfile or not code:
        messagebox.showerror("Invalid", "All fields are required!")
        return

    if not os.path.isfile(mainfile):
        messagebox.showerror("Invalid", "Source file does not exist!")
        return

    try:
        out = PdfWriter()
        file = PdfReader(mainfile)
        
        

        for idx in range(len(file.pages)):
            page = file.pages[idx]
            out.add_page(page)

        # Set password
        out.encrypt(code)
        with open(protectfile, "wb") as f:
            out.write(f)

        messagebox.showinfo("Success", "PDF file protected successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

Protect = Button(
    root,
    text="Protect PDF Files",
    compound=LEFT,
    image=Button_icon,
    width=230,
    height=50,
    bg="#bfb9b9",
    command=protect
)
Protect.pack(side=BOTTOM, pady=40)

root.mainloop()
