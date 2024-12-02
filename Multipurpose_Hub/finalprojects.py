from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfWriter, PdfReader  # type: ignore
import pyttsx3  # type: ignore
from datetime import date
import os

def age_calculator():
    root = Tk()
    root.geometry("800x600")
    root.resizable(False, False)
    root.title("Age Calculator")

    photo = PhotoImage(file="ageimage.png")
    myImage = Label(image=photo)
    myImage.pack(padx=15, pady=15)

    Label(text="Name", font=23).place(x=200, y=250)
    Label(text="Year", font=23).place(x=200, y=300)
    Label(text="Month", font=23).place(x=200, y=350)
    Label(text="Date", font=23).place(x=200, y=400)

    nameValue = StringVar()
    yearValue = StringVar()
    monthValue = StringVar()
    dateValue = StringVar()

    nameEntry = Entry(textvariable=nameValue, width=30, bd=3)
    yearEntry = Entry(textvariable=yearValue, width=30, bd=3)
    monthEntry = Entry(textvariable=monthValue, width=30, bd=3)
    dateEntry = Entry(textvariable=dateValue, width=30, bd=3)

    nameEntry.place(x=300, y=250)
    yearEntry.place(x=300, y=300)
    monthEntry.place(x=300, y=350)
    dateEntry.place(x=300, y=400)

    def calculate_age():
        today = date.today()
        try:
            birth_day = int(dateEntry.get())
            birth_month = int(monthEntry.get())
            birth_year = int(yearEntry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers!")
            return

        current_day, current_month, current_year = today.day, today.month, today.year
        age = current_year - birth_year

        if (current_month < birth_month) or (current_month == birth_month and current_day < birth_day):
            age -= 1

        months = current_month - birth_month
        if months < 0:
            months += 12

        days = current_day - birth_day
        if days < 0:
            prev_month = current_month - 1 if current_month > 1 else 12
            prev_year = current_year if current_month > 1 else current_year - 1
            days += (date(prev_year, prev_month + 1, 1) - date(prev_year, prev_month, 1)).days
            months -= 1

        Label(
            text=f"{nameValue.get()}, your age is {age} years, {months} months, {days} days.",
            font=50
        ).place(x=300, y=500)

    Button(text='Calculate Age', font=20, bg="black", fg="white", height=2, command=calculate_age).place(x=300, y=450)
    root.mainloop()

def text_to_speech():
    root = Tk()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female  
    engine.setProperty('rate',120)

    def speak_now():
        engine.say(textv.get())
        engine.runAndWait()

    obj = LabelFrame(root, text="Text to Speech", font=20, bd=1, bg="lightblue1", fg="black")
    obj.pack(fill="both", expand="yes", padx=10, pady=10)

    Label(obj, text="Text", font=30, bg="lightblue1").pack(side=LEFT)

    textv = StringVar()
    Entry(obj, textvariable=textv, font=30, width=35, bd=5).pack(side=LEFT, padx=10)

    Button(obj, text="Speak", bg="crimson", fg="white", bd=3, command=speak_now).pack(side=LEFT, padx=15)

    root.title("Text to Speech")
    root.geometry("600x200")
    root.resizable(False,False)
    root.mainloop()

def pdf_password_protector():
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


def main():
    print("Choose an application to run:")
    print("1. Age Calculator")
    print("2. Text to Speech")
    print("3. PDF Password Protector")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        age_calculator()
    elif choice == "2":
        text_to_speech()
    elif choice == "3":
        pdf_password_protector()
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
