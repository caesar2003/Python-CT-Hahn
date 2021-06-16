from time import time, sleep
import tkinter as tk
from tkinter import *
import os


root = tk.Tk()
def ampel():
    time= 5000
    root.after(time, orange)
    root.after(time, greenremove)
    time+=2000
    root.after(time, red)
    root.after(time, orangeremove)
    time += 9000
    root.after(time, orange)
    time += 1000
    root.after(time, redremove)
    root.after(time, orangeremove)
    root.after(time, green)
def orange():
    gelb = tk.Frame(root, bg="yellow")
    gelb.place(relwidth=0.2, relheight=0.2, relx=0.3, rely=0.1)
def orangeremove():
    gelb = tk.Frame(root, bg="white")
    gelb.place(relwidth=0.2, relheight=0.2, relx=0.3, rely=0.1)
def red ():
    rot = tk.Frame(root, bg="red")
    rot.place(relwidth=0.2, relheight=0.2, relx=0.1, rely=0.1)
def redremove ():
    rot = tk.Frame(root, bg="white")
    rot.place(relwidth=0.2, relheight=0.2, relx=0.1, rely=0.1)
def green():
    grün = tk.Frame(root, bg="green")
    grün.place(relwidth=0.2, relheight=0.2, relx=0.5, rely=0.1)
def greenremove ():
    grün = tk.Frame(root, bg="white")
    grün.place(relwidth=0.2, relheight=0.2, relx=0.5, rely=0.1)

canvas = tk.Canvas(root, height=700, width=700, bg="white")
canvas.pack()

frame= tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


grün= tk.Frame(root, bg="green")
grün.place(relwidth=0.2, relheight=0.2, relx=0.5, rely=0.1)


taster = tk.Button(root, text="Ampel umschalten", padx=10, pady=5, fg="white", bg="#482ce8", command=ampel)
taster.pack()

root.mainloop()