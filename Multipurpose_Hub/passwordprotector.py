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
