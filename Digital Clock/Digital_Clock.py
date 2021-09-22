from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

def quit(*args):
    root.destroy()


def Dig_Clock_Time():
    time = datetime.datetime.now()
    time = (time.strftime("%Y-%m-%d %H:%M:%S"))
    
    txt.set(time)
    root.after(1000, Dig_Clock_Time)


root = Tk()
root.attributes("-fullscreen", False)
root.configure(background='black')
root.bind("X", quit)
root.after(1000, Dig_Clock_Time)

fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()