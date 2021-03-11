from tkinter import *
import tkinter as tk
import track
import cv2
import numpy as np
import draw
import people_count
import keyboard
import ctypes 

def menu(low,high): 
    def adjustWindow(window):
        w = 1000
        h = 750
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        window.geometry('%dx%d+%d+%d' % (w,h,x,y))
        window.resizable(False,False)

    def create(n):
        for i in range(1,n+1):
            Label(start, text="Player {}".format(i), bg='light blue').place(x=150, y=200+i*50)
            en = Entry(start)
            en.place(x=350, y=200+i*50)
            #if 'entry' not in en:
            entries.append(en)
            #else:
        button=Button(start,text="Start",command=hallo).place(x=500,y=600)

    def hallo():
        p=1
        for entry in entries:
            if entry.get():
                names.append(entry.get())
                p+=1
            else:
                #ctypes.windll.user32.MessageBoxW(0, "Please enter player name", "Dialogue Box", 0)
                names.append('Player {}'.format(p))
                p+=1
        print(names)

                
        start.destroy()
        people_count.count(names,low,high)
    entries=[]
    names=[]
    opt=[1,2,3,4,5]
    start = Tk()
    start.title("Select your choice")
    adjustWindow(start)
    Label(start, text="Enter player details", width='50', height="3", font=("Calibri", 30,'bold'), fg='white', bg='purple', anchor = CENTER).place(x=-80, y=-40)
    Label(start, text="", bg='light blue', width='400', height='500').place(x=0, y=100)
    variable = StringVar(start)
    variable.set(1) # default value
    Label(start, text="Select number of players", bg='light blue').place(x=300, y=150)
    drop = OptionMenu(start, variable,*opt,command=create).place(x=500, y=150)
    start.mainloop() 
