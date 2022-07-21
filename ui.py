import tkinter as tk
import options as op
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()
root.title("Pharmacy Sign-Language Communication App")


photoSyringe = tk.PhotoImage(file="assets/Images/syringe-solid.png")
photoCapsules = tk.PhotoImage(file="assets/Images/capsules-solid.png")
photoClock = tk.PhotoImage(file="assets/Images/clock-solid.png")
photoList = tk.PhotoImage(file="assets/Images/list-solid.png")
myFont = tk.font.Font(family="Times")


def showDoses():
    frameUseMethod.place_forget()
    frameSpecialInstructions.place_forget()
    frameGeneralInstructions.place_forget()
    frameDoses.place(relwidth=0.85, relheight=1, relx=0)

def showUseMethod():
    frameDoses.place_forget()
    frameSpecialInstructions.place_forget()
    frameGeneralInstructions.place_forget()
    frameUseMethod.place(relwidth=0.85, relheight=1, relx=0)

def showSpecialInstructions():
    frameUseMethod.place_forget()
    frameDoses.place_forget()
    frameGeneralInstructions.place_forget()
    frameSpecialInstructions.place(relwidth=0.85, relheight=1, relx=0)

def showGeneralInstructions():
    frameUseMethod.place_forget()
    frameDoses.place_forget()
    frameSpecialInstructions.place_forget()
    frameGeneralInstructions.place(relwidth=0.85, relheight=1, relx=0)


#main window frame
root.minsize(1000, 700)
frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=1)


#sidebar frame
frameSideBar = tk.Frame(frame, bg="gray")
frameSideBar.place(relwidth=0.13, relheight=1, relx=0.85)


#main screen frames
frameDoses = tk.Frame(frame, bg="red")
frameDoses.place(relwidth=0.85, relheight=1, relx=0)

frameUseMethod = tk.Frame(frame, bg="black")
frameSpecialInstructions = tk.Frame(frame, bg="white")
frameGeneralInstructions = tk.Frame(frame, bg="white")


#sidebar buttons
sh1 = tk.Button(frameSideBar, image=photoSyringe, padx=0, pady=20, fg="black", font=myFont, command=showDoses)
sh1.pack()

sh2 = tk.Button(frameSideBar, image=photoCapsules, padx=0, pady=20, fg="black", font=myFont, command=showUseMethod)
sh2.pack()

sh3 = tk.Button(frameSideBar, image=photoClock, padx=0, pady=20, fg="black", font=myFont, command=showSpecialInstructions)
sh3.pack()

sh4 = tk.Button(frameSideBar, image=photoList, padx=0, pady=20, fg="black", font=myFont, command=showGeneralInstructions)
sh4.pack()


#labels

lblDoses = tk.Label(frameDoses, text="الجرعات", bg="gray", fg="black", font="Arial, 40", pady=15)
lblDoses.pack()

lblUseMethod = tk.Label(frameUseMethod, text="طريقة الاستخدام", bg="gray", fg="black", font="Arial, 40", pady=15)
lblUseMethod.pack()

lblSpecialInstructions = tk.Label(frameSpecialInstructions, text="تعليمات خاصة", bg="white", fg="black", font="Arial, 40", pady=15)
lblSpecialInstructions.pack()

lblGeneralInstructions = tk.Label(frameGeneralInstructions, text="تعليمات عامة", bg="white", fg="black", font="Arial, 40", pady=15)
lblGeneralInstructions.pack()



#Doses content
clicked = tk.StringVar(value=op.doseType[0])
clicked1 = tk.StringVar(value=op.doseCount[0])
clicked2 = tk.StringVar(value=op.doseFreq[0])
clicked3 = tk.StringVar(value=op.doseDur[0])
clicked4 = tk.StringVar(value=op.doseTime[0])
  
# initial menu text
# clicked.set(op.doseCount[0])
# clicked.set(op.doseFreq[0])
# clicked.set(op.doseDur[0])
# clicked.set(op.doseTime[0])

droplbl = tk.Label(frameDoses, text="نوع الدواء", bg="white", fg="black", font="Arial, 20")
droplbl.pack()
drop = ttk.OptionMenu(frameDoses, clicked, clicked.get(), *op.doseType, bootstyle='dark')
# drop.config(fg="black")
drop.pack()

drop2lbl = tk.Label(frameDoses, text="العدد", bg="white", fg="black", font="Arial, 20")
drop2lbl.pack()
drop = ttk.OptionMenu(frameDoses, clicked1, clicked1.get(), *op.doseCount, bootstyle='dark')
drop.pack()

drop3bl = tk.Label(frameDoses, text="التكرار", bg="white", fg="black", font="Arial, 20")
drop3bl.pack()
drop = ttk.OptionMenu(frameDoses, clicked2, clicked2.get(), *op.doseFreq, bootstyle='dark')
drop.pack()

drop3bl = tk.Label(frameDoses, text="المدة", bg="white", fg="black", font="Arial, 20")
drop3bl.pack()
drop = ttk.OptionMenu(frameDoses, clicked3, clicked3.get(), *op.doseDur, bootstyle='dark')
drop.pack()

drop3bl = tk.Label(frameDoses, text="وقت الجرعة", bg="white", fg="black", font="Arial, 20")
drop3bl.pack()
drop = ttk.OptionMenu(frameDoses, clicked4, clicked4.get(), *op.doseTime, bootstyle='dark')
drop.pack()

root.mainloop()