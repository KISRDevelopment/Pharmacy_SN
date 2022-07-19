import tkinter as tk
import options as op
import ttkbootstrap as ttk
#from ttkbootstrap.constants import *

root = tk.Tk()


photo1 = tk.PhotoImage(file = r"assets/Images/syringe-solid.png")
myFont = tk.font.Font(family="Times")


def show1():
    frame2.place_forget()
    frame3.place(relwidth=0.9, relheight=1, relx=0)

def show2():
    frame3.place_forget()
    frame2.place(relwidth=0.9, relheight=1, relx=0)

root.minsize(1000, 700)
frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=1)

frame1 = tk.Frame(frame, bg="black")
frame1.place(relwidth=0.1, relheight=1, relx=0.9)

frame2 = tk.Frame(frame, bg="red")
frame2.place(relwidth=0.9, relheight=1, relx=0)

frame3 = tk.Frame(frame, bg="blue")
#frame2.place(relwidth=0.9, relheight=1, relx=0.1)

sh1 = tk.Button(frame1, text="الجرعات", image=photo1, padx=10, pady=5, fg="gray", bg="white", compound = ttk.TOP, font=myFont, command=show1)
sh1.pack()

sh2 = tk.Button(frame1, text="طريقة الاستخدام", padx=10, pady=5, fg="gray", bg="white", command=show2)
sh2.pack()

sh3 = tk.Button(frame1, text="تعليمات خاصة", padx=10, pady=5, fg="gray", bg="white", command=show2)
sh3.pack()

sh4 = tk.Button(frame1, text="تعليمات عامة", padx=10, pady=5, fg="gray", bg="white", command=show2)
sh4.pack()

clicked = tk.StringVar()
  
# initial menu text
clicked.set(op.options[0])

drop = tk.OptionMenu(frame2, clicked, *op.options)
drop.config(fg="black")
drop.place(rely=0.1, relx=0.1)

root.mainloop()