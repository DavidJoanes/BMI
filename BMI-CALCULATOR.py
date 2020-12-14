from tkinter import *
from tkinter import messagebox
import tkinter.messagebox

def calculate():
    a = float(entry1.get())
    b = float(entry2.get())
    try:
        bmi = a/pow(b, 2)
        entry3.delete(0, END)
        entry3.insert(0, bmi)
    except ZeroDivisionError:
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry3.insert(0, "ERROR!")
    bmi = a/pow(b, 2)
    if bmi >= 18.5 and bmi < 25.0:
        entry4.delete(0, END)
        entry4.insert(0, "You are very healthy.")
    elif bmi >= 25.0 and bmi < 30.0:
        entry4.delete(0, END)
        entry4.insert(0, "You are overweight.")
    elif bmi > 30.0:
        entry4.delete(0, END)
        entry4.insert(0, "YOU ARE OBESE!!  Please see a Doctor!")
    else:
        entry4.delete(0, END)
        entry4.insert(0, "You are underweight!")
    statusbar.config(text=" Status: |  Operation succeeded")

def refresh():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    statusbar.config(text=" Status: |  Refreshed at 0s")

def exit():
    Exit = tkinter.messagebox.askyesno("Simple BMI Calculator", "Confirm exit")
    if Exit > 0:
        root.destroy()
    else:
        return


root = Tk()
root.title("BMI Calculator")
root.iconbitmap("calculator.ico")
root.geometry("470x310")
root.resizable(False, False)
root.configure()

frame = Frame(root)
frame.grid()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu, tearoff=False)
mymenu.add_cascade(label="Menu", menu=submenu)
submenu.add_command(label="Refresh", command=refresh)
submenu.add_separator()
submenu.add_command(label="Exit", command=exit)


text1 = Label(frame, text="Enter your weight (in Kg)", font=("arial", 13, "bold"))
text1.grid(row=0, column=0, pady=6, padx=2)
entry1 = Entry(frame, font=("new times roman", 13, "bold"), justify=RIGHT)
entry1.grid(row=1, column=0, pady=6, ipady=3)

text2 = Label(frame, text="Enter your height (in m)", font=("arial", 13, "bold"))
text2.grid(row=2, column=0, pady=6, padx=2)
entry2 = Entry(frame, font=("new times roman", 13, "bold"), justify=RIGHT)
entry2.grid(row=3, column=0, pady=6, ipady=3)

calculate1 = Button(frame, text="Calculate", font=("consolas", 13, "bold"), bd=3, command=lambda:calculate())
calculate1.grid(row=3, column=1)

text3 = Label(frame, text="Your BMI is:", font=("arial", 13, "bold"))
text3.grid(row=4, column=0, pady=6, padx=2)
entry3 = Entry(frame, font=("new times roman", 13, "bold"), justify=RIGHT)
entry3.grid(row=4, column=1, pady=6, ipady=3)

unit = Label(frame, text="Kg/m^2", font=("arial", 9, "bold"))
unit.grid(row=4, column=2)

name = Label(frame, text="  BODY MASS INDEX", font=("agency", 15, "bold"), fg="red")
name.grid(row=1, column=1)

entry4 = Entry(frame, font=("calibri", 13, "bold"), width=45)
entry4.grid(row=5, column=0, pady=10, ipady=3, columnspan=4)

statusbar = Label(root, text=" Status: |  Ready", bd=3, relief=SUNKEN, anchor=W, width=66)
statusbar.grid(row=6, column=0, pady=8)





root.mainloop()